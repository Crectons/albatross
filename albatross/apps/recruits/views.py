from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.exceptions import NotAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .filters import PostTreeFilter, PostInfoFilter
from .models import PostInfo, PostTree, PostResume
from .serializers import PostInfoListSerializer, PostInfoDetailSerializer, PostInfoCreateSerializer, \
    PostResumeSerializer
from .serializers import PostTreeSerializer, PostTreeDetailSerializer


class PostInfoViewSet(ModelViewSet):
    """
    岗位信息视图
    """
    queryset = PostInfo.objects.all().order_by('pid')  # 获取 pid 排序的查询集，便于分页
    serializer_class = PostInfoListSerializer
    permission_classes = [AllowAny]  # 允许任何人访问 TODO:权限控制
    # 过滤排序
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_class = PostInfoFilter
    ordering_fields = ['pid', 'recommend', 'salary_max', 'salary_min', 'update_time']

    def get_serializer_class(self):
        """
        获取序列化器类
        """
        if self.action == 'list':
            return PostInfoListSerializer
        if self.action == 'retrieve':
            return PostInfoDetailSerializer
        return PostInfoCreateSerializer

    @action(methods=['post'], detail=True)
    def deliver(self, request, pk=None):
        """
        投递岗位
        """
        post_info = self.get_object()
        user = request.user
        if not user.is_authenticated:
            raise NotAuthenticated('用户未登录')

        resume = PostResume.objects.create(post=post_info, user=user)
        serializer = PostResumeSerializer(resume)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostTreeViewSet(ModelViewSet, CacheResponseMixin):
    """
    岗位分类视图
    """
    filterset_class = PostTreeFilter  # 自定义过滤器
    pagination_class = None  # 关闭分页
    permission_classes = [AllowAny]  # 允许任何人访问

    # 指定要输出的数据来自哪个查询集
    def get_queryset(self):
        """
        根据请求的行为，过滤不同的行为对应的序列化器需要的数据
        """
        if self.action == 'list':
            return PostTree.objects.filter(father=None)  # 只有当 pid=None 返回的是省级数据
        else:
            return PostTree.objects.all()

    # 指定序列化器
    def get_serializer_class(self):
        """
        根据请求的行为，指定不同的序列化器
        """
        if self.action == 'list':
            return PostTreeSerializer
        else:
            return PostTreeDetailSerializer

    @action(methods=['get'], detail=False)
    def all(self, request):
        queryset = self.filter_queryset(PostTree.objects.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PostTreeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostTreeSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def tree(self, request):
        """
        获取岗位分类树, 列表视图
        """
        res = []

        info = PostTree.objects.all()  # 所有岗位分类信息
        for node_1 in info.filter(father=None):  # 一级节点遍历
            res.append({  # 返回数据格式
                'id': node_1.id,
                'name': node_1.name,
                'children': []
            })
            node_1_children = res[-1]['children']  # 该一级节点的子节点列表

            for node_2 in info.filter(father=node_1):  # 二级节点遍历
                node_1_children.append({
                    'id': node_2.id,
                    'name': node_2.name,
                    'children': []
                })
                node_2_children = node_1_children[-1]['children']

                for node_3 in info.filter(father=node_2):  # 三级节点遍历
                    node_2_children.append({
                        'id': node_3.id,
                        'name': node_3.name
                    })

        return Response(res)

    @action(methods=['get'], detail=False)
    def dict(self, response):
        """
        获取岗位分类字典, 列表视图
        """
        res = {}
        info = PostTree.objects.all()

        for item in info:
            res.update({  # 返回数据格式
                item.id: item.name
            })

        return Response(res)

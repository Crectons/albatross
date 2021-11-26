from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PostInfo, PostTree
from .serializers import PostInfoSerializer, PostTreeSerializer


class PostInfoViewSet(ModelViewSet):
    """
    岗位信息视图
    """
    queryset = PostInfo.objects.all().order_by('pid')  # 获取 pid 排序的查询集，便于分页
    serializer_class = PostInfoSerializer
    permission_classes = [AllowAny]  # 允许任何人访问 TODO:权限控制


class PostTreeViewSet(ModelViewSet):
    """
    岗位分类视图
    """
    queryset = PostTree.objects.all().order_by('id')  # 获取 id 排序的查询集
    serializer_class = PostTreeSerializer
    filter_fields = ('id', 'type', 'name')
    pagination_class = None  # 关闭分页
    permission_classes = [AllowAny]  # 允许任何人访问

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

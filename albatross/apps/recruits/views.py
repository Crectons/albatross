from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PostInfo, PostTree
from .serializers import PostInfoSerializer, PostTreeSerializer


class PostInfoViewSet(ModelViewSet):
    queryset = PostInfo.objects.all().order_by('pid')
    serializer_class = PostInfoSerializer
    permission_classes = [AllowAny]


class PostTreeViewSet(ModelViewSet):
    queryset = PostTree.objects.all().order_by('id')
    serializer_class = PostTreeSerializer
    filter_fields = ('id', 'type', 'name')
    pagination_class = None
    permission_classes = [AllowAny]

    @action(methods=['get'], detail=False)
    def tree(self, request):
        res = []

        info = PostTree.objects.all()
        for node_1 in info.filter(father=None):
            res.append({
                'id': node_1.id,
                'name': node_1.name,
                'children': []
            })
            node_1_children = res[-1]['children']

            for node_2 in info.filter(father=node_1):
                node_1_children.append({
                    'id': node_2.id,
                    'name': node_2.name,
                    'children': []
                })
                node_2_children = node_1_children[-1]['children']

                for node_3 in info.filter(father=node_2):
                    node_2_children.append({
                        'id': node_3.id,
                        'name': node_3.name
                    })

        return Response(res)

    @action(methods=['get'], detail=False)
    def dict(self, response):
        res = {}
        info = PostTree.objects.all()

        for item in info:
            res.update({
                item.id: item.name
            })

        return Response(res)

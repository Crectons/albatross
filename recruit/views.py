from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PostInfo, PostTree
from .serializers import PostInfoSerializer, PostTreeSerializer


class PostInfoViewSet(ModelViewSet):
    queryset = PostInfo.objects.all()
    serializer_class = PostInfoSerializer


class PostTreeViewSet(ModelViewSet):
    queryset = PostTree.objects.all()
    serializer_class = PostTreeSerializer

    @action(methods=['get'], detail=False)
    def tree(self, request):
        res = []
        ban_list_2 = ['产品规划', '产品研发', '电商产品设计']
        ban_list_3 = ['产品']

        info = PostTree.objects.all()
        for node_1 in info.filter(father=None):
            res.append({
                'id': node_1.id,
                'name': node_1.name,
                'children': []
            })
            node_1_children = res[-1]['children']

            for node_2 in info.filter(father=node_1):
                if node_2.name in ban_list_2:
                    continue
                node_1_children.append({
                    'id': node_2.id,
                    'name': node_2.name,
                    'children': []
                })
                node_2_children = node_1_children[-1]['children']

                for node_3 in info.filter(father=node_2):
                    if node_3.name in ban_list_3:
                        continue
                    node_2_children.append({
                        'id': node_3.id,
                        'name': node_3.name
                    })

        return Response(res)

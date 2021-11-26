from rest_framework import serializers
from . import models


class AreaInfoSer(serializers.ModelSerializer):
    """
    省市区信息序列化
    """
    class Meta:
        model = models.Areas
        fields = ('id', 'name')


class NextAreasInfoSer(serializers.ModelSerializer):
    # 嵌套序列化器，得到自己想要的数据
    addinfo = AreaInfoSer(many=True, read_only=True)

    # 这个是返回字符串显示的是__str__方法返回的内容。
    # addinfo = serializers.StringRelatedField(many=True, read_only=True)
    # 不写的时候默认是PrimaryKeyrelatedField，也就是显示id

    # 要展现他的下一级
    class Meta:
        model = models.Areas
        fields = ('id', 'name', 'addinfo')


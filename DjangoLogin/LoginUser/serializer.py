from rest_framework import serializers
from LoginUser.models import *
class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Goods
        fields=[
            "goods_number",
            "goods_name",
            "goods_price",
            "goods_count",
            "goods_location",
            "goods_safe_date",
            "goods_pro_time",
        ]

class Userbiao(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginUser
        fields = [
            "email",
            "password",
            "username",
            "photo",
            "age",
            "gender",
            "address",
        ]
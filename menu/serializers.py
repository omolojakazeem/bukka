from rest_framework import serializers
from dish.serializers import DishCreateSerializer,DishListSerializer
from .models import DishItem



class MenuListSerializer(serializers.ModelSerializer):
    dish = DishCreateSerializer()

    class Meta:
        model = DishItem
        fields = '__all__'


class MenuCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DishItem
        fields = ('customer', 'dish', 'quantity',)


class MenuEditSerializer(serializers.ModelSerializer):
    dish = DishCreateSerializer()

    class Meta:
        model = DishItem
        fields = '__all__'
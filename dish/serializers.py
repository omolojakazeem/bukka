from rest_framework import serializers
from .models import DishCategory, Dish


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory
        fields = '__all__'


class DishListSerializer(serializers.ModelSerializer):
    category = DishCategorySerializer()
    class Meta:
        model = Dish
        fields = '__all__'


class DishCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

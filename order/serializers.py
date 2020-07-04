from rest_framework import serializers
from .models import Order
from menu.serializers import MenuListSerializer,MenuCreateSerializer,MenuEditSerializer

from menu.models import DishItem


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('sold','ordered_date','amount')


class OrderListSerializer(serializers.ModelSerializer):
    menu = MenuListSerializer(many=True)
    amount = serializers.ReadOnlyField(source='get_amount')

    class Meta:
        model = Order
        fields = '__all__'


class OrderEditSerializer(serializers.ModelSerializer):
    menu = MenuEditSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'





from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Customer
from accounts.serializers import UserSerializer,UserCustomerSerializer

from accounts.models import User


class CustomerCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        exclude = ('full_name',)


class CustomerListSerializer(serializers.ModelSerializer):
    user = UserCustomerSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

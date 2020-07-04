from .models import User
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import User

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    extra_kwargs = {'password': {'write_only': True,
                                 'input_type': 'password',}}
    confirm_password = serializers.CharField(allow_blank=False, write_only=True,
                                             style={'input_type': 'password',})

    password = serializers.CharField(allow_blank=False,style={'input_type': 'password',})

    class Meta:
        model = User
        fields = ('password','email','confirm_password')


class UserCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)



from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerCreateSerializer, CustomerListSerializer

# Create your views here.
from accounts.models import User


class CustomerListView(generics.GenericAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerListSerializer
        if self.request.method == 'POST':
            return CustomerCreateSerializer


    def get(self, request, *args, **kwargs):
        customer = Customer.objects.all()
        serializer = CustomerListSerializer(customer, many=True)
        customer_data = serializer.data
        context = {
            'Customers': customer_data
        }
        return Response(context)


    def post(self, request, *args, **kwargs):
        customer_data = request.data
        serializer = CustomerCreateSerializer(data=customer_data)
        if serializer.is_valid(raise_exception=True):
            user_data = serializer.validated_data['user']
            email = user_data['email']
            password = user_data['password']
            confirm_password = user_data['confirm_password']
            if password == confirm_password:
                user = User(
                    email=email,
                    user_type="CUSTOMER"
                )

                user.set_password(password)
                user.save()
                customer_data_save = serializer.save(user=user)
                return Response({
                    "Success": "You have successfully created the {} Menu".format(customer_data_save.full_name)
                })

            else:
                return Response({
                    "Failed": "Password does not match"
                })


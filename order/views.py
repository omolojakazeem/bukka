from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Order
from .serializers import OrderCreateSerializer, OrderListSerializer, OrderEditSerializer


class OrderListView(generics.GenericAPIView):

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return OrderListSerializer
        else:
            return OrderCreateSerializer


    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        serializer = OrderListSerializer(order, many=True)
        order_data = serializer.data
        context = {
            'Menus': order_data
        }
        return Response(context)

    def post(self, request, *args, **kwargs):
        order_data = request.data
        serializer = OrderCreateSerializer(data=order_data)
        if serializer.is_valid(raise_exception=True):
            #vendor = Vendor.objects.get(user=request.user)
            order_data_save = serializer.save()
            return Response(order_data_save,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return OrderEditSerializer
        else:
            return OrderListSerializer

    def get_object(self, pk):
        try:
            menu = Order.objects.get(pk=pk)
            return menu
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        my_order = self.get_object(pk)
        order_serializer = OrderListSerializer(my_order, many=False)
        return Response(order_serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        my_order = self.get_object(pk)
        my_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        order_data = request.data
        my_order = self.get_object(pk)
        order_serializer = OrderEditSerializer(my_order, data=order_data)

        if order_serializer.is_valid():
            order = order_serializer.save()
            return Response(order_serializer.data,status=status.HTTP_200_OK)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

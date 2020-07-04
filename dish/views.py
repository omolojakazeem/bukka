from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Dish, DishCategory
from .serializers import DishCreateSerializer,DishListSerializer, DishCategorySerializer


class DishListView(generics.GenericAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DishListSerializer
        if self.request.method == 'POST':
            return DishCreateSerializer


    def get(self, request, *args, **kwargs):
        dish = Dish.objects.all()
        serializer = DishListSerializer(dish, many=True)
        dish_data = serializer.data
        context = {
            'Dishes': dish_data
        }
        return Response(context)


    def post(self, request, *args, **kwargs):
        dish_data = request.data
        serializer = DishCreateSerializer(data=dish_data)
        if serializer.is_valid(raise_exception=True):
            #vendor = Vendor.objects.get(user=request.user)
            dish_data_save = serializer.save()
            return Response({
                "Success": "You have successfully created the {} Menu".format(dish_data_save.name)
            })


class DishDetailView(generics.GenericAPIView):
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return DishCreateSerializer
        elif self.request.method == 'GET':
            return DishListSerializer
        else:
            return DishListSerializer

    def get_object(self, pk):
        try:
            dish = Dish.objects.get(pk=pk)
            return dish
        except Dish.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        my_dish = self.get_object(pk)
        dish_serializer = DishListSerializer(my_dish, many=False)
        return Response(dish_serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        my_dish = self.get_object(pk)
        my_dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        dish_data = request.data
        my_dish = self.get_object(pk)
        dish_serializer = DishCreateSerializer(my_dish, data=dish_data)

        if dish_serializer.is_valid():
            dish = dish_serializer.save()
            return Response(dish_serializer.data,status=status.HTTP_200_OK)
        return Response(dish_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DishCategoryView(generics.GenericAPIView):
    serializer_class = DishCategorySerializer

    def get(self, request,*args, **kwargs):
        dish_category = DishCategory.objects.all()
        serializer = DishCategorySerializer(dish_category, many=True)
        category_data = serializer.data
        context = {
            'Dish Category': category_data
        }
        return Response(context)

    def post(self, request, *args, **kwargs):
        dish_category = request.data
        serializer = DishCategorySerializer(data=dish_category)
        if serializer.is_valid(raise_exception=True):
            # vendor = Vendor.objects.get(user=request.user)
            category_data_save = serializer.save()
            return Response({
                "Success": "You have successfully created the {} Menu".format(category_data_save.category_name)
            })
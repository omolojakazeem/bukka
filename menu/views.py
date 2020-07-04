from django.http import Http404
# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from .models import DishItem
from .serializers import MenuCreateSerializer, MenuListSerializer


class MenuListView(generics.GenericAPIView):
    serializer_class = MenuCreateSerializer

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return MenuListSerializer
        else:
            return MenuCreateSerializer


    def get(self, request, *args, **kwargs):
        menu = DishItem.objects.all()
        serializer = MenuListSerializer(menu, many=True)
        menu_data = serializer.data
        context = {
            'Menus': menu_data
        }
        return Response(context)

    def post(self, request, *args, **kwargs):
        menu_data = request.data
        serializer = MenuCreateSerializer(data=menu_data)
        if serializer.is_valid(raise_exception=True):
            #vendor = Vendor.objects.get(user=request.user)
            dish_id = serializer.validated_data['menu'].id
            if dish_id:

                menu_data_save = serializer.save()
            return Response({
                "Success": "You have successfully created the {} Menu".format(menu_data_save.customer)
            })


class MenuDetailView(generics.GenericAPIView):
    serializer_class = MenuListSerializer

    def get_object(self, pk):
        try:
            menu = DishItem.objects.get(pk=pk)
            return menu
        except DishItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        my_menu = self.get_object(pk)
        menu_serializer = MenuListSerializer(my_menu, many=False)
        return Response(menu_serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        my_menu = self.get_object(pk)
        my_menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        order_data = request.data
        my_menu = self.get_object(pk)
        menu_serializer = MenuListSerializer(my_menu, data=order_data)

        if menu_serializer.is_valid():
            menu = menu_serializer.save()
            return Response(menu_serializer.data,status=status.HTTP_200_OK)
        return Response(menu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
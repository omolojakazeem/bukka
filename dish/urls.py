from django.urls import path

from .views import DishListView,DishDetailView,DishCategoryView

urlpatterns = [
    path('',DishListView.as_view(), name='dish_list'),
    path('detail/<pk>',DishDetailView.as_view(), name='dish_detail'),
    path('category/',DishCategoryView.as_view(), name='dish_category')
]
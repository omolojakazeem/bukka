from django.urls import path

from .views import MenuListView, MenuDetailView

urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),
    path('detail/<pk>', MenuDetailView.as_view(), name='menu_detail')
]

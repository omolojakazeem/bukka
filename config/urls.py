from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/dishes/', include('dish.urls')),
    path('api/v1/menus/', include('menu.urls')),
    path('api/v1/orders/', include('order.urls')),
    path('api/v1/customers/', include('customer.urls')),
]
from django.contrib import admin
from .models import Dish,DishCategory
# Register your models here.


admin.site.register(DishCategory)
admin.site.register(Dish)
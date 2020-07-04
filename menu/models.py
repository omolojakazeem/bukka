from django.conf import settings
from django.db import models

# Create your models here.
from dish.models import Dish


class DishItem(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    dish = models.ForeignKey(Dish, related_name='menu', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    sold = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        total = self.quantity*self.dish.price
        return total

    def __str__(self):
        return str(self.customer)
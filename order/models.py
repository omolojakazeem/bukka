from django.conf import settings
from django.db import models
from menu.models import DishItem


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='order', on_delete=models.CASCADE, null=True, blank=True)
    ordered_date = models.DateTimeField(null=True,blank=True)
    menu = models.ManyToManyField(DishItem)
    sold = models.BooleanField(default=False)
    amount = models.FloatField(default=0)

    @property
    def get_amount(self):
        amount=0
        for total in self.menu.all():
            amount += total.get_total_price
        return round(amount,2)

    def __str__(self):
        return self.amount

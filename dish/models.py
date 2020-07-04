from django.db import models


class DishCategory(models.Model):
    category_name = models.CharField(max_length=50, default='swallow')

    def __str__(self):
        return self.category_name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)

    def __str__(self):
      return self.name

from django.conf import settings
from django.db import models

# Create your models here.
from phone_field import PhoneField


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = PhoneField()


    @property
    def get_slug_name(self):
        full_name = self.first_name + '_' + self.last_name
        return full_name

    def get_full_name(self, first_name, last_name):
        full_name = first_name + ' ' + last_name
        return full_name

    def save(self, *args, **kwargs):
        self.full_name = self.get_full_name(self.first_name, self.last_name)
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name
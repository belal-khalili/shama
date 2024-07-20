from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    meli_code = models.CharField(max_length=10)


# class profile_info(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     id_number = models.CharField(max_length=20)
#     occupation = models.CharField(max_length=50, blank=True)
#     address = models.CharField(max_length=100)
#     street_number = models.CharField(max_length=10)
#     flat_number = models.CharField(max_length=10, blank=True)
#     zip_code = models.CharField(max_length=10)
#     city = models.CharField(max_length=10)
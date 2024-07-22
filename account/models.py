from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    meli_code = models.CharField(max_length=10)



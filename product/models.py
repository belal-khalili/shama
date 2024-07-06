from django.db import models
class Company(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255 , null = True , blank = True)
    phone = models.CharField(max_length = 20 , null = True , blank = True)
    email = models.EmailField(null = True , blank = True)
    def __str__(self) :
        return self.name
class Product(models.Model) :
    name = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    description = models.TextField()
    brand = models.CharField(max_length = 255 , null = True , blank = True)
    price = models.CharField(max_length = 255)
    stock = models.IntegerField()
    available = models.BooleanField()
    provider_company = models.ForeignKey(Company , on_delete = models.CASCADE , null = True , blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    rating = models.FloatField(null = True , blank = True)
    def __str__(self) :
        return self.name
    

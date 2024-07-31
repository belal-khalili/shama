from django.db import models
from category.models import Category
def slug_maker(name):
    name = list(name)
    for i in range(len(name)):
        if name[i] == " " :
            name.pop(i)
            name.insert(i , "_")
    name = "".join(name)

class Company(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255 , null = True , blank = True)
    phone = models.CharField(max_length = 20 , null = True , blank = True)
    email = models.EmailField(null = True , blank = True)
    class Meta() :
        verbose_name_plural = "کمپانی ها"
    def __str__(self) :
        return self.name
    
class Product(models.Model) :
    name = models.CharField(max_length = 255)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    brand = models.CharField(max_length = 255 , null = True , blank = True)
    price = models.CharField(max_length = 255)
    slug = models.SlugField(null = True , blank = True)
    stock = models.IntegerField()
    available = models.BooleanField()
    provider_company = models.ForeignKey(Company , on_delete = models.CASCADE , null = True , blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    rating = models.FloatField(null = True , blank = True)
    image = models.ImageField(upload_to = "product" , null = True , blank = True)

    class Meta() :
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"
    def __str__(self) :
        return self.name
    

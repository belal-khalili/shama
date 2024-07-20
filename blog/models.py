from django.db import models

# Create your models here.


class Single_blog(models.Model):
    title=models.CharField(max_length=100)
    rating=models.FloatField(null = True )
    views=models.IntegerField()
    slug=models.SlugField()
    date=models.DateField()
    description=models.TextField()
    def __str__(self) -> str:
        return self.title
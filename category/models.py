from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True,blank=True)
    def __str__(self) -> str:
        return self.title
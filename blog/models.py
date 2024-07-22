from django.db import models

class Single_blog(models.Model):
    title=models.CharField(max_length=100)
    rating=models.FloatField(null = True )
    views=models.IntegerField()
    slug=models.SlugField()
    date=models.DateField()
    description=models.TextField()
    created=models.DateTimeField(auto_now_add = True , null = True , blank = True)
    image = models.ImageField(upload_to = "blog" , null = True , blank = True)
    def __str__(self) -> str:
        return self.title

from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=120)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    text = models.TextField()
    admin_response = models.TextField(null=True, blank=True)
    is_read_by_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=120)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    text = models.TextField()
    admin_response = models.TextField(null=True, blank=True)
    is_read_by_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "contact" , null = True , blank = True)
    class Meta():
        verbose_name_plural = "پیام ها"
    def __str__(self):
        return self.subject
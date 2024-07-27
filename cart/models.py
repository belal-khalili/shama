from django.db import models
from product.models import Product
from account.models import User
# Create your models here.
class Cart(models.Model):
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user.email} ({self.is_paid})'



class CartDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.product.name} /  {self.cart.user.email}'
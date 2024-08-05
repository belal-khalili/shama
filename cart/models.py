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

    def cart_total_price(self):
        total_price = 0
        this_cart_items = self.cartitem_set.all()
        for item in this_cart_items:
            total_price += item.cartitem_total_price()
        return total_price



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.product.name} /  {self.cart.user.email}'
    
    def cartitem_total_price(self):
        return int(self.product.price) * int(self.amount)

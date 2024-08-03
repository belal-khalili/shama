from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('' , views.cart , name = "cart_page") ,
    path('add-to-cart/<int:product_id>' , views.add_to_cart , name = "add_to_cart_page") ,
    path('update-cart-item-quantity' , views.update_cart_item_quantity , name = "update-cart-item-quantity")
]
    

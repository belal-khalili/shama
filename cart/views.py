from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from product.models import Product
from account.models import User
from .models import Cart, CartItem
# Create your views here.
def add_to_cart(request, product_id):
    user_cart,cart_exsits = Cart.objects.get_or_create(user_id=request.user.id, is_paid=False)
    if cart_exsits == False:
        # for item in user_cart
        product = Product.objects.filter(id=product_id).first()
        new_cart_item,cart_item_exists = CartItem.objects.get_or_create(cart=user_cart,product=product)
        if cart_item_exists == False:
            new_cart_item.amount += 1
            new_cart_item.save()
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'error'})


def cart(request):
    return render(request, 'cart/cart.html')
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
    user_cart = Cart.objects.get(user=request.user.id, is_paid=False)
    cart_items = user_cart.cartitem_set.all()
    return render(request, 'cart/cart.html', {'cartitems': cart_items, 'cart':user_cart})


def update_cart_item_quantity(request):
    if request.method == "POST" :
        cart_item_id = request.POST.get('cart_item_id')
        action = request.POST.get('action')
        # print(cart_item_id)
        # print(action)
        
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            
            if action == 'increment':
                cart_item.amount += 1
            elif action == 'decrement':
                cart_item.amount -= 1
            
            if cart_item.amount <= 0:
                cart_item.delete()
                return JsonResponse({'status': 'deleted'})
            else:
                cart_item.save()
                return JsonResponse({'status': 'updated', 'quantity': cart_item.amount})
        
        except CartItem.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'CartItem not found'}, status=404)

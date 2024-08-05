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

from django.conf import settings
import requests
import json
from django.shortcuts import redirect
import datetime

#? sandbox merchant 
# if settings.SANDBOX:
sandbox = 'sandbox'
# else:
# sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'


def send_request(request):
    # amount = 100000  # Rial / Required
    amount = Cart.objects.get(user=request.user, is_paid=False).cart_total_price()

    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    try:
        response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                # return JsonResponse({'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']})
                url = ZP_API_STARTPAY + str(response['Authority'])
                return redirect(url)
            else:
                return HttpResponse({'status': False, 'code': str(response['Status'])})
        return response
    
    except requests.exceptions.Timeout:
        return HttpResponse({'status': False, 'code': 'timeout'})
    except requests.exceptions.ConnectionError:
        return HttpResponse({'status': False, 'code': 'connection error'})


def verify(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": Cart.objects.get(user=request.user, is_paid=False).cart_total_price(),
        "Authority": request.GET['Authority'],
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            cart = Cart.objects.get(user=request.user, is_paid=False)
            cart.is_paid = True

            cart.payment_date=datetime.datetime.today()
            cart.save()
            # return HttpResponse({'status': True, 'RefID': response['RefID']})
            return HttpResponse('<h1>okey your payment is successful!</h1>')
        else:
            return HttpResponse({'status': False, 'code': str(response['Status'])})
    return response
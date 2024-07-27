from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from product.models import Product

# Create your views here.
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if product:
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'not found'})


def cart(request):
    return HttpResponse('cart page')
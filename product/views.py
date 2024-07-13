from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def product(request):
    data = Product.objects.all()
    paginator = Paginator(data,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'product/product.html',{'products':page_obj,'paginator':paginator})
    
def single_product(request , id):
    data = Product.objects.get(id = id)
    if data.available == True :
        return render(request , "product/single-product.html" , {"product" : data})

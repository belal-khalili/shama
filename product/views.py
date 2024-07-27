from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def product_list(request):
    data = Product.objects.all()
    paginator = Paginator(data, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'product/product.html',{'page_obj':page_obj,'paginator':paginator})
    
def single_product(request , slug):
    data = Product.objects.get(slug = slug)
    if data.available == True :
        return render(request , "product/single-product.html" , {"product" : data})


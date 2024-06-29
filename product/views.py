from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def product(request):
    data = Product.objects.all()
    paginator = Paginator(data,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'product/product.html',{'products':page_obj,'paginator':paginator})


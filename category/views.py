from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator
# Create your views here.



def category_page(request,cat_name):
    data = Product.objects.filter(category__link=cat_name)
    paginator= Paginator(data,2)
    page_number=request.GET.get("page")
    this_page=paginator.get_page(page_number)
    print(data)
    return render(request, 'category/category.html',{"this_page" : this_page , "paginator" : paginator})
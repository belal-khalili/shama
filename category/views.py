from django.shortcuts import render
from product.models import Product
# Create your views here.
def category_page(request,cat_name):
    data = Product.objects.filter(category__link=cat_name)
    print(data)
    return render(request, 'category/category.html',{'products':data} )
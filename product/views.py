from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def product_list(request):
    data = Product.objects.all()
    paginator = Paginator(data, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
<<<<<<< HEAD

    return render(request,'product/product.html', {'page_obj' : page_obj , 'paginator' : paginator})


=======
    return render(request,'product/product.html',{'products':page_obj,'paginator':paginator})
    
>>>>>>> 7ed3781f563c02db9eaa68446697fda31f83f901
def single_product(request , id):
    data = Product.objects.get(id = id)
    if data.available == True :
        return render(request , "product/single-product.html" , {"product" : data})


from django.shortcuts import render
from .models import Single_blog
from django.core.paginator import Paginator
def blog_page(request):
    data = Single_blog.objects.all()
    conditional_data = Single_blog.objects.order_by("created")[0 : 4]
    paginator = Paginator(data , 1)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    return render(request , "blog/blog.html" , {"this_page" : this_page ,"paginator" : paginator.page_range, "newest_single_blogs" : conditional_data})
def single_blog_page(request , slug):
    data = Single_blog.objects.get(slug = slug)
    conditional_data = Single_blog.objects.order_by("created")[0 : 4]
    return render(request , "blog/single_blog.html" , {"single_blog" : data , "newest_single_blogs" : conditional_data})


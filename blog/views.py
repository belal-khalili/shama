from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
def blog_page(request):
    data = Article.objects.all()
    conditional_data = Article.objects.order_by("created")[0 : 4]
    paginator = Paginator(data , 6)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    return render(request , "blog/blog.html" , {"this_page" : this_page ,"paginator" : paginator.page_range, "newest_articles" : conditional_data})
def single_blog_page(request , slug):
    data = Article.objects.get(slug = slug)
    return render(request , "single_blog.html" , {"article" : data})
from django.shortcuts import render
from .models import Single_blog


def blog(request):
    # data= Single_blog.objects.all()
    return render(request, "blog/blog.html")



# def Single_blog(request, slug):
#     data= Single_blog.objects.get(slug=slug)
#     return render(request,"blog/single-blog.html",{"single_blog" : data} )
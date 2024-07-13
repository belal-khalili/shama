from django.shortcuts import render
from category.models import Category
# Create your views here.
def home_page(request):
    categorys = Category.objects.all() 
    return render(request, 'home/home.html', {'categorys':categorys})
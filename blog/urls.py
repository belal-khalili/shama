from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("" , views.blog_page , name = "blog_page") ,
    path("<slug:slug>" , views.single_blog_page , name = "single_blog_page")
]


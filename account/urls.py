from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('',views.profile,name='profile_page'),
    path('sefareshha/',views.sefareshha,name='sefareshha_page'),
    path('darkhastmarjui/',views.darkhastmarjui,name='darkhastmarjui_page'),
    path('favoritelist/',views.favoritelist,name='favoritelist_page'),
    path('nazarat/',views.nazarat,name='nazarat_page'),
    path('adresses/',views.adresses,name='adresses_page'),
    path('bazdidakhir/',views.bazdidakhir,name='bazdidakhir_page'),
    path('userinfo/',views.userinfo,name='userinfo_page'),

    path('register/',views.register,name='register_page')


]
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('contact/',include('contact.urls')),
    path('products/',include('product.urls')),
    # path('product/',include('product.urls')),
    path('account/',include('account.urls')),
    path('cat/',include('category.urls')),
    path('blog/',include('blog.urls')),
    path('profile/',include('user_profile.urls')),
    path('cart/',include('cart.urls')),
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT) 
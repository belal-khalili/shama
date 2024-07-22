from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# this funciton is temporary and should not be continued
def show_user_info(request):
    return HttpResponse(request.user.password)


def profile(request):
    return render(request, 'user_profile/profile.html')

def sefareshha(request):
    return render(request, 'user_profile/sefareshha.html')
    
def darkhastmarjui(request):
    return render(request, 'user_profile/darkhastmarjui.html')

def favoritelist(request):
    return render(request, 'user_profile/favoritelist.html')

def nazarat(request):
    return render(request, 'user_profile/nazarat.html')

def adresses(request):
    return render(request, 'user_profile/adresses.html')

def bazdidakhir(request):
    return render(request, 'user_profile/bazdidakhir.html')

def userinfo(request):
    return render(request, 'user_profile/userinfo.html')


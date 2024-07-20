from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegisterForm,LoginForm
from .models import User
from django.contrib.auth import login,logout
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user_email = request.POST.get('email')
                user = User.objects.filter(email__iexact=user_email).first()
                print(user)
                if user == None:
                    print('no user with that email')
                    user_password = request.POST.get('password')
                    new_user = User(email=user_email,username=user_email)
                    new_user.set_password(user_password)
                    new_user.save()
                else:
                    form.add_error('email','ایمیل داده شده تکراری است')
                    return render(request, 'account/register.html',{'form':form})
            else:
                return render(request, 'account/register.html',{'form':form})
            
        return render(request, 'account/register.html',{'form':RegisterForm})
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = request.POST.get('email')
            user_password = request.POST.get('password')
            user = User.objects.get(email__iexact=user_email)
            password_corrct = user.check_password(user_password)
            if password_corrct:
                login(request,user)
                return redirect(reverse('home_page'))
            else:
                print('error')
        
    return render(request, 'account/register.html',{'form':RegisterForm})


def profile(request):
    return render(request, 'account/account.html')

def sefareshha(request):
    return render(request, 'account/sefareshha.html')
    
def darkhastmarjui(request):
    return render(request, 'account/darkhastmarjui.html')

def favoritelist(request):
    return render(request, 'account/favoritelist.html')

def nazarat(request):
    return render(request, 'account/nazarat.html')

def adresses(request):
    return render(request, 'account/adresses.html')

def bazdidakhir(request):
    return render(request, 'account/bazdidakhir.html')

def userinfo(request):
    return render(request, 'account/userinfo.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('home_page'))
    
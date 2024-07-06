from django.shortcuts import render
from .forms import RegisterForm
from .models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_email = request.POST.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            print(user)
            if user == None:
                print('no user with that email')
            else:
                print('this email si not unique')
                form.add_error('email','ایمیل داده شده تکراری است')
                return render(request, 'account/register.html',{'form':form})
        else:
            return render(request, 'account/register.html',{'form':form})
        
    return render(request, 'account/register.html',{'form':RegisterForm})
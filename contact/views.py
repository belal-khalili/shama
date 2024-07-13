from django.shortcuts import render
from .forms import ContactModelForm
def contact(request):
    if request.method == 'POST':
        print(request.POST)
        form = ContactModelForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request,'contact/contact.html',{'form':form})
    return render(request,'contact/contact.html',{'form':ContactModelForm})
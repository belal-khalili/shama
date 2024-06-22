from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject')
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            text = request.POST.get('text')

            new_contact = Contact(subject=subject,full_name=full_name,email=email,phone_number=phone_number,text=text)
            new_contact.save()
        else:
            return render(request,'contact/contact.html',{'form':form})

    return render(request,'contact/contact.html',{'form':ContactForm})
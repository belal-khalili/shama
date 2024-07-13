from django import forms
from .models import Contact

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["subject" , "full_name" , "email" , "phone_number" , "text" , "image"]
        labels = {"subject" : "موضوع" , "full_name" : "نام و نام خانوادگی" , "email" : "ایمیل" , "phone_number" : "شماره تماس" , "text" : "متن پیام"}
        widgets = {
        "subject" : forms.TextInput(attrs = {'class':'form-control'}) ,
        "full_name" : forms.TextInput(attrs = {'class':'form-control'}) ,
        "email" : forms.EmailInput(attrs = {'class':'form-control' , 'placeholder':'example@test.com'}) ,
        "phone_number" : forms.TextInput(attrs = {'class':'form-control'}) ,
        "text" : forms.Textarea(attrs = {'class':'form-control' , 'rows':6}) 
        }
        error_messages = {
            "email" : {"required" : "لطفا ایمیل خود را وارد کنید" , "invalid" : "لطفا مثل بچه آدم ایمیل خود را وارد کنید"}
        }
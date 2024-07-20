from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل',
    widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'لطفا ایمیل خود را وارد نمایید'})
    )
    password = forms.CharField(label='پسورد',
    widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'لطفا گذرواژه خود را وارد نمایید'
    })
                               )
    confirm_password = forms.CharField(label='تایید پسورد',
    widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'لطفا گذرواژه خود را تکرار نمایید'
    })
)


    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('رمز عبور و تکرار آن باهم مطابق نیستند')
        else:
            return password
        

class LoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل',
    widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'لطفا ایمیل خود را وارد نمایید'}))
    password = forms.CharField(label='پسورد',widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'لطفا گذرواژه خود را وارد نمایید'}))
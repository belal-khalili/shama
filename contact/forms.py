from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=120,label='موضوع',widget=forms.TextInput(attrs={
        'class':'form-control '
    }))
    full_name = forms.CharField(max_length=120,label='نام و نام خانوادگی',widget=forms.TextInput(attrs={
        'class':'form-control '
    }))
    email = forms.EmailField(label='ایمیل',error_messages={'required':'لطفا ایمیل خود را وارد کنید','invalid':'لطفا مثل بچه آدم ایمیل خود را وارد کنید'},widget=forms.EmailInput(attrs={
        'class':'form-control ',
        'placeholder':'example@test.com'
    }))
    phone_number = forms.CharField(max_length=13,label='شماره تماس',widget=forms.TextInput(attrs={
        'class':'form-control '
    }))
    text = forms.CharField(label='متن پیام',widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':6
    }))
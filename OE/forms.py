from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField()
    email = forms.EmailField(required=True,label='Your e-mail address')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class LoginForm(forms.Form):
     username=forms.CharField()
     password = forms.CharField(max_length=32, widget=forms.PasswordInput)


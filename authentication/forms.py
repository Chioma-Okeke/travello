from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password', 'remember_me')
    
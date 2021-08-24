from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Order


# class CreatUserFor(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']
# 		


class LoginForm(forms.Form):
	Username= forms.Charfield()
	password = forms.Charfield(widget=forms.passwordInput)

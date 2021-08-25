from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm



# def RegisterPage(request):
# 	form = UserCreationForm()
# 	context = {'form':form}
# 	return render(request, '', context)


def user_login(request):
	context = {}
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
		else:
			form = LoginForm()
			
	context['form'] = form
	return render(request, '', context)
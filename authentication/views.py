from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm


# Create your views here.
# def loginPage(request):
# 	form = UserCreationForm()
# 	context = {'form':form}
# 	return render(request, '', context)


# def RegisterPage(request):
# 	form = UserCreationForm()
# 	context = {'form':form}
# 	return render(request, '', context)
def user_login(request):
	if request.method == 'POST':
		form = LoginFOrm(requrst.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_actgive:
					login(request, user)
					return HttpResponse('Authenticated')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
		else:
			form = LoginForm()
		return render(request, '', {'form': form})
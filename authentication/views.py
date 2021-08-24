from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, RegistrationForm


# Create your views here.
def registration_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    context={}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'authentication/signup.html', context)

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
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
		return render(request, 'authentication/signin.html', {'form': form})
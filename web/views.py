from django.shortcuts import render, redirect

from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'full_name':    form.cleaned_data['name'],
                'email':        form.cleaned_data['email'],
                'message':      form.cleaned_data['message']
            }
            message = '\n\n'.join(body.values())
            form.save()
            # try:
            #     send_mail(subject, message, 'iamkomolafe.o.s@gmail.com', ['iamkomolafe.o.s@gmail.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return redirect("home")
        context['form'] = form
    form = ContactForm

    context['form'] = form

    return render(request, 'contact.html', context)

def news(request):
    return render(request, 'news.html')
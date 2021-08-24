from django.urls import path, include
from .views import home, about, contact, news


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('news/', news, name='news'),
    path('authentication/', include('authentication.urls'))

]
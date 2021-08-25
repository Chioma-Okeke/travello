from django.urls import path

from .views import registration_view, user_login

urlpatterns = [
    path('signup/', registration_view, name='signup'),
    path('signin/', user_login, name='signin')
]

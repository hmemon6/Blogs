from django.urls import path, include
from . import views




app_name ='accounts'

urlpatterns = [
    # Include default auth urls. Like login but we still need a template for it
    path('',include('django.contrib.auth.urls')),
    # path for registration page its also default form but still need a template. see view and register.html
    path('register/',views.register, name='register'),
]

from django.conf.urls import include, url
from .views import *
    
    # las urls empiezan a aca 
    
urlpatterns = [
    url(r'^$', main, name="main"),
    url(r'register/', register, name="register")
    ]
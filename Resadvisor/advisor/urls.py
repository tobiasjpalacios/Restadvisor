from django.conf.urls import include, url
from .views import *
    
    # las urls empiezan a aca 
    
urlpatterns = [
    url(r'^$', main, name="main"),
    url(r'register/', register, name="register"),
    url(r'maps/', maps, name="maps"),
    url(r'^upload$', upload, name="upload"),
    url(r'^login/', my_login, name="login"),
    url(r'^logout/', my_logout, name="logout"),
    url(r'^signup/$', signup, name='signup'),
    url(r'^comentar/',new_comentario, name="comentar"),
]
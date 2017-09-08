from django.conf.urls import include, url
from . import views
    
    # las urls empiezan a aca 
    
urlpatterns = [
    url(r'^$', views.main),
    ]
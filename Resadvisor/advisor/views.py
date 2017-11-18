# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required 
from django.core.urlresolvers import reverse 
from django.shortcuts import render_to_response, render, redirect 
from django.template import RequestContext 
from django.conf import settings 
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import AnonymousUser 
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q 
from datetime import datetime, timedelta 
from django.utils import timezone
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from .forms import SignUpForm
# Create your views here.


def main(request):
    restaurantes = Restaurante.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'advisor/main.html',{'restaurantes': restaurantes})

def register(request):
    return render(request, 'advisor/register.html')

def login(request):
    return render(request, 'advisor/register.html')

def maps(request):
    return render(request, 'advisor/maps.html')

def upload(request):
    title = request.POST.get("titl")
    name = request.POST.get("nombr")
    descripcion = request.POST.get("descr")
    direcc = request.POST.get("direcci")
    new = Restaurante(titl=titl, name=name , descripcion=descripcion, direcc=direcc)
    new.save()
    return redirect(main)
    
    
def new_comentario(request):
    texto=request.post.get("textocomentario")
    new_comentario =Comentarios(texto=texto)
    new_comentario.save()
    return redirect(main)
    
def my_logout(request):
    logout(request)
    return redirect ('main')

def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('main') 
    else:
        print redirect('main')
        
        
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'main.html', {'form': form})
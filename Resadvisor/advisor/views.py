# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *

# Create your views here.


def main(request):
    return render(request, 'advisor/main.html')

def register(request):
    return render(request, 'advisor/register.html')

def login(request):
    return render(request, 'advisor/register.html')

def maps(request):
    return render(request, 'advisor/maps.html')

def upload(request):
    titl = request.POST.get("titl")
    name = request.POST.get("nombr")
    descripcion = request.POST.get("descr")
    direcc = request.POST.get("direcci")
    new = Restaurante(title=titl, name=name , descripcion=descripcion, direcc=direcc)
    new.save()
    return redirect(main)
    
    
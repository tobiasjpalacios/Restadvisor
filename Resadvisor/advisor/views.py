# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'advisor/main.html')

def register(request):
    return render(request, 'advisor/register.html')

def login(request):
    return render(request, 'advisor/register.html')

def maps(request):
    return render(request, 'advisor/maps.html')

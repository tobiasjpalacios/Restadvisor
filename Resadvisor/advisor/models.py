# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone 

# Create your models here.
class Restaurante(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=140, default='DEFAULT VALUE')
    descripcion = models.TextField()
    direcc = models.TextField()
    
class Comentarios(models.Model):
    autor = models.ForeignKey('auth.user')
    text  = models.TextField()
    rest_comen = models.ForeignKey('Restaurante',on_delete=models.CASCADE,)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    
    def publish(self):
            self.published_date = timezone.now()
            self.save()

            
    def __str__(self):
            return self.text 

class Puntaje(models.Model):
    puntajetotal=models.BigIntegerField()
    perfil_puntuado=models.ForeignKey('Perfil',on_delete=models.CASCADE)
    
        
class Perfil(models.Model):
    categoria=models.CharField(max_length=100)
    

class Likes(models.Model):
    cant_likes =models.BigIntegerField()
    like_target= models.ForeignKey('Restaurante',on_delete=models.CASCADE,)
    like_owner= models.ForeignKey('Perfil',on_delete=models.CASCADE,)
    
    

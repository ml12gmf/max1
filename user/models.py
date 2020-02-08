from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    data_di_nascita = models.DateField()
    sesso = models.CharField(max_length=200)
    email = models.EmailField()
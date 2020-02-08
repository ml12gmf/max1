from django.db import models

# Create your models here.
class Recipe(models.Model):
	nome        = models.CharField(max_length= 120)
	tipo        = models.CharField(max_length=9)
	autore      = models.CharField(max_length= 120)
	difficolta  = models.CharField(max_length= 9)
	descrizione = models.TextField()
	immagine    = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
	ingredienti = models.TextField()
	nazionalita = models.CharField(max_length=50)
from django.db import models

# Create your models here
class Ingredient(models.Model):
	nome = models.CharField(max_length=50)
	calorie = models.PositiveIntegerField()
from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):
	nome        = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"nome"}))
	tipo        = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"antipasto, primo, secondo, contorno, dolce"}))
	autore      = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"username"}))
	difficolta  = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"facile, media, difficile"}))
	descrizione = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"descrizione"}))
	immagine    = forms.ImageField(required=True, widget=forms.TextInput(attrs={"placeholder":"immagine"}))
	ingredienti = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"lista ingredienti necessari per la ricetta con relative quantita"}))
	nazionalita = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"luogo di origine della ricetta"}))
	
	class Meta:
		model = Recipe
		fields = [
		   'nome',
		   'tipo',
		   'autore',
		   'difficolta',
		   'descrizione',
		   'immagine',
		   'ingredienti',
		   'nazionalita'
		]  
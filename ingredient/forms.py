from django import forms

from .models import Ingredient

class IngredientForm(forms.ModelForm):
	nome    = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"nome dell'ingrediente"}))
	calorie = forms.DecimalField(required=True, widget=forms.TextInput(attrs={"placeholder":"calorie per grammo"}))
	class Meta:
		model = Ingredient
		fields = [
		   'nome',
		   'calorie'
		   ]
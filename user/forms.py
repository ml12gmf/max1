from django import forms

from .models import User

class UserForm(forms.ModelForm):
	nome = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"nome"}))
	cognome = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"cognome"}))
	data_di_nascita = forms.DateField(required=False, widget=forms.TextInput(attrs={"placeholder":"data di nascita"}))
	sesso = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"M/F"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder":"email"}))

	class Meta:
		model = User
		fields = [
		'nome',
		'cognome',
		'data_di_nascita',
		'sesso',
		'email'

		]  
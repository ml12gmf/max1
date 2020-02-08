from django.shortcuts import render

# Create your views here.
from .models import Ingredient
from .forms import IngredientForm
from django.views.generic import ListView

def ingredient_create_view(request):
	form = IngredientForm(request.POST or None) 
	if form.is_valid():
		form.save()
		form = IngredientForm()

	context = {
	  'form':form
   }

	return render(request,"ingredient/templates/ingredient_create.html", context)


class IngredientList(ListView):
	model = Ingredient
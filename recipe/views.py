from django.shortcuts import render

# Create your views here.
from .models import Recipe
from .forms import RecipeForm
from django.views.generic import ListView

def recipe_create_view(request):
	form = RecipeForm(request.POST or None) 
	if form.is_valid():
		form.save()
		form = RecipeForm()

	context = {
	  'form':form
   }

	return render(request,"recipe/templates/recipe_create.html", context)

class RecipeList(ListView):
	model = Recipe
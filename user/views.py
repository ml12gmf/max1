from django.shortcuts import render

# Create your views here.
from .models import User
from .forms import UserForm
from django.views.generic import ListView

def user_create_view(request):
	form = UserForm(request.POST or None) 
	if form.is_valid():
		form.save()
		form = UserForm()

	context = {
	  'form':form
   }

	return render(request,"user/templates/user_create.html", context)

class UserList(ListView):
	model = User
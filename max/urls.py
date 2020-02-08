"""max URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ingredient.views import ingredient_create_view, IngredientList

from recipe.views import recipe_create_view, RecipeList

from user.views import user_create_view, UserList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredient/create/', ingredient_create_view ),
    path('ingredient/list/', IngredientList.as_view()),
    path('recipe/create/', recipe_create_view),
    path('recipe/list/', RecipeList.as_view()),
    path('user/create/', user_create_view),
    path('user/list/', UserList.as_view()),


]

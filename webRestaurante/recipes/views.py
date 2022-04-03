from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Recipe


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    paginate_by = 100

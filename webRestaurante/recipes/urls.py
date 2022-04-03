from django.urls import path
from recipes.views import RecipeListView


recipe_urlpatterns = ([
    path('', RecipeListView.as_view(), name='recipe_list')
], 'recipe')

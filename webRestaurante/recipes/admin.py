from django.contrib import admin
from .models import Recipe


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Recipe, RecipeAdmin)

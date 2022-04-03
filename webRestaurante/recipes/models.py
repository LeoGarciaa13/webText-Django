from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subititulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'receta'
        verbose_name_plural = 'recetas'
        ordering = ['-created']

    def __str__(self):
        return self.title

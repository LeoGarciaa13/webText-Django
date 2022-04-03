from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'



# Create your views here.
# def home(request):
#     return render(request, 'core/home.html')

def historia(request):
    return render(request, 'core/historia.html')

def visit(request):
    return render(request, 'core/visit.html')

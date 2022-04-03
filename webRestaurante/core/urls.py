from django.urls import path
from core import views
from core.views import HomePageView

core_urlpatterns = ([
    #path('', views.home, name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('historia/', views.historia, name='historia'),
    path('visit/', views.visit, name='visit'),
], 'core')

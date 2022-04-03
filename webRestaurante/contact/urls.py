from django.urls import path
from contact.views import ContactFormView
from django.views.generic import TemplateView


contact_urlpatterns = ([
    path('', ContactFormView.as_view(), name='contact'),
    path('thanks/', TemplateView.as_view(
        template_name="contact/thanks.html"), name='thanks'),
], 'contact')

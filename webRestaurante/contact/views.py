from django.shortcuts import render
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        print(name)
        return super().form_valid(form)

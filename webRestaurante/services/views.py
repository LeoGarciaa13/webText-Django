from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Service


# Create your views here.
class ServiceListView(ListView):
    model = Service
    paginate_by = 100


class ServiceCreateView(CreateView):
    model = Service
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('service:service_list')


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['title', 'subtitle', 'content', 'image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('service:update', args=[self.object.id]) + '?ok'


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('service:service_list')

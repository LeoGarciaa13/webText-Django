from django.urls import path
from services.views import ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView

service_urlpatterns = ([
    path('', ServiceListView.as_view(), name='service_list'),
    path('create/', ServiceCreateView.as_view(), name='create'),
    path('update/<int:pk>', ServiceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ServiceDeleteView.as_view(), name='delete'),
], 'service')

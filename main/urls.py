from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.about_us, name='about_us'),
    path('prices/', views.prices, name='prices'),
    path('services/', views.services, name='services'),
    
]
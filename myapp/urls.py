from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('event/', views.event, name='event'),
    path('faculty/', views.faculty, name='faculty'),
    path('contact/', views.contact, name='contact'),
]

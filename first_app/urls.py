from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('django_forms/', views.django_forms, name='django_forms'),
]

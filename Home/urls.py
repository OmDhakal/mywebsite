from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('contact/', views.contact, name='contact'),
]
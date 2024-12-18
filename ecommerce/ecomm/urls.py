from django.contrib import admin
from django.urls import path
from ecomm import views 


urlpatterns = [
    path('', views.add_product ,name='home')
]

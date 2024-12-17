from django.shortcuts import render
from django.http import HttpResponse
from ecomm import models
from .models import product

# Create your views here.
def home (request):
    return render(request, 'index.html')


def product(request):
    products = product.objects.all()
    return render(request , 'index.html', { 'product': product})

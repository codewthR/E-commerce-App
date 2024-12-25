from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .models import product
from django.http import JsonResponse

def add_product(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        price =data.get('price')
        image = request.FILES.get('image')
        product.objects.create(
            name= name,
            price=price,
            image=image,
        )
    return render(request, 'index.html')



def display(request):
    if request.method == "GET":
        products = product.objects.all()
        return render(request, "display.html" , {'products' : products})
    
    


def updates(request, id):
    if request.method == 'PUT':
        return render(request, "updates.html")








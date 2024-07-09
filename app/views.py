from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'home.html', context)

def about (request):
    return render(request, 'about.html')

def products (request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'products.html', context)

def about (request):
    return render(request, 'contact.html')

def about (request):
    return render(request, 'skincare.html')

def about (request):
    return render(request, 'haircare.html')
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    kategories = Kategori.objects.all()
    context = {"products" : products, "kategories" : kategories}
    return render(request, 'home.html', context)

def about(request):
    kategori = Kategori.objects.all()
    context = {"kategori" : kategori}
    return render(request, 'about.html', context)

def products(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'products.html', context)

def contact(request):
    kategories = Kategori.objects.all()
    if request.method == "POST":
        name = request.POST["firstname"]
        surname = request.POST["lastname"]
        email = request.POST["email"]
        comment = request.POST["comment"]

        Contact(
            contact_name= name,
            contact_surname = surname,
            contact_email = email,
            contact_description = comment
        ).save()
    context = {"kategories" : kategories}
    return render(request, 'contact.html', context)

def skincare(request):
    return render(request, 'skincare.html')

def haircare(request):
    return render(request, 'haircare.html')

def detailproduct(request, id):
    productDetail = Product.objects.get(pk=id)
    kategories = Kategori.objects.all()
    context = {"productDetail": productDetail, "kategories" : kategories}
    return render(request, 'detailproduct.html', context) 

def detailkategori(request, slug):
    kategoriDetail = Kategori.objects.get(kategori_slug=slug)
    kategories = Kategori.objects.all()
    kategoriProducts = Product.objects.filter(product_category=kategoriDetail)
    context = {"kategoriDetail": kategoriDetail, "kategories" : kategories, "kategoriProducts" : kategoriProducts}
    return render(request, 'detailkategori.html', context) 
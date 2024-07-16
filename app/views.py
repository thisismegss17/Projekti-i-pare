from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    products = Product.objects.all()
    kategories = Kategori.objects.all()
    context = {"products" : products, "kategories" : kategories}
    return render(request, 'home.html', context)

def about(request):
    kategories = Kategori.objects.all()
    context = {"kategories" : kategories}
    return render(request, 'about.html', context)

def products(request):
    kategories = Kategori.objects.all()
    products = Product.objects.all()
    context = {"products" : products, "kategories" : kategories,}
    return render(request, 'products.html', context)

def contact(request):
    kategories = Kategori.objects.all()
    if request.method == "POST":
        name_ = request.POST["firstname"]
        surname = request.POST["lastname"]
        email = request.POST["email"]
        comment = request.POST["comment"]
    # if name_ !="" and surname !="" and email !="" and comment !="" :
        Contact(
            contact_name= name_,
            contact_surname = surname,
            contact_email = email,
            contact_description = comment
        ).save()
        messages.success(request, "Message sended!")
    # else:
    #     messages.error(request, "Message not sended!")
    context = {"kategories" : kategories}
    return render(request, 'contact.html', context)


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
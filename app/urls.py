from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="homePage"),
   path("about/", views.about, name="aboutPage"),
   path("products/", views.products, name="productPage"),
   path("contact/", views.contact, name="contactPage"),
   path("skincare/", views.skincare, name="skincarePage"),
   path("haircare/", views.haircare, name="haircarePage"),
   path("detailproduct/<id>", views.detailproduct, name="detailproductPage"),
   path("kategori/<slug>", views.detailkategori, name="detailkategoriPage")
]

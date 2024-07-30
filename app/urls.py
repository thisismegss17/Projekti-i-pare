from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="homePage"),
   path("about/", views.about, name="aboutPage"),
   path("products/", views.products, name="productPage"),
   path("contact/", views.contact, name="contactPage"),
   path("detailproduct/<id>", views.detailproduct, name="detailproductPage"),
   path("kategori/<slug>", views.detailkategori, name="detailkategoriPage"),
   # Auth
    path("register/", views.register, name="registerPage"),
    path("login/", views.login, name="loginPage"),
    path("logout/", views.logout, name= "logout"),
    path("accessLogin/", views.accessLogin, name= "accessLoginPage"),
]

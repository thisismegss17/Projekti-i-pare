from django.db import models

# Create your models here.

class Kategori(models.Model):
    kategori_name = models.CharField(max_length=300, null=True, blank=True)       
    kategori_image = models.ImageField(upload_to='about/', null=True, blank=True)
    kategori_slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.kategori_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.TextField(max_length=1000, null=True, blank=True)
    product_price = models.DecimalField( max_digits=5, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(upload_to='product/', null=True, blank=True)
    product_category = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.product_name}"


class Contact(models.Model):
    contact_name = models.CharField(max_length=200, null=True, blank=True)
    contact_surname = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"

class FormContact(models.Model):
    formContact_name = models.CharField(max_length=250, null=True, blank=True)
    formContact_surname = models.CharField(max_length=250, null=True, blank=True)
    formContact_email = models.EmailField(null=True, blank=True)
    formContact_comment = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f"{self.formContact_name} {self.formContact_surname}"
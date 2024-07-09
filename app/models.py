from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.TextField(max_length=1000, null=True, blank=True)
    product_price = models.DecimalField( max_digits=5, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(upload_to='product/', null=True, blank=True)

    def __str__(self):
        return f"{self.product_name}"
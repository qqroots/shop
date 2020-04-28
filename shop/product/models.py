from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    product_price = models.DecimalField(max_digits = 3, decimal_places = 0)
    product_stock = models.DecimalField(max_digits = 3, decimal_places = 0, default = 100)

    def __str__(self):
        return self.product_name
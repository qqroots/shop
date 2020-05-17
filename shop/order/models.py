from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    order_user = models.DecimalField(max_digits = 10, decimal_places = 0) #查user id 用__set看看
    # order_amount = models.DecimalField(max_digits=6,decimal_places=0)
    order_total = models.DecimalField(max_digits=6,decimal_places=0)


class OrderItem(models.Model):
    product_name = models.CharField(max_length = 50)
    product_price = models.DecimalField(max_digits = 3, decimal_places = 0)
    product_qty = models.IntegerField()
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

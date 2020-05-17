from django.contrib import admin
from .models import Order,OrderItem

class OrderAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Order._meta.fields]
    list_display = ['id','order_user','order_total']
    ordering = ('id',)
    search_fields = ('order_user ','id')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]
    ordering = ('id',)

# Register your models here.

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)

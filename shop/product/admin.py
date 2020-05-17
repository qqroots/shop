from django.contrib import admin
from .models import Product

class ProduceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    ordering = ('id',)

# Register your models here.
admin.site.register(Product)
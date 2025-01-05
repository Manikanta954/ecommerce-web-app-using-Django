from django.contrib import admin

from .models import Electronics
@admin.register(Electronics)

class ElectronicAdmin(admin.ModelAdmin):
    list_display=('product_name','price')
    

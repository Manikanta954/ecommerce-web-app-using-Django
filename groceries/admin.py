from django.contrib import admin

# Register your models here.
from .models import Groceries
@admin.register(Groceries)

class GroceriesAdmin(admin.ModelAdmin):
    list_display=('product_name','price','quantity')
from django.contrib import admin


from .models import Fashion
@admin.register(Fashion)

class FashionAdmin(admin.ModelAdmin):
    list_display=('product_name','price')
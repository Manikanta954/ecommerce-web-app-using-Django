from django.db import models

# Create your models here.
class Groceries(models.Model):
    product_name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    quantity=models.CharField(max_length=12)
    
    def __str__(self):
        return f"{self.product_name}{self.price}"
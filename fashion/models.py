from django.db import models

class Fashion(models.Model):
    product_name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.product_name}{self.price}"
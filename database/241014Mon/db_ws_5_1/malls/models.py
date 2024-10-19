from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    product = models.ManyToManyField('Product')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
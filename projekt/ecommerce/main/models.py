from django.db import models
from django.core.validators import RegexValidator
from datetime import timedelta

# Create your models here.
class Warranty(models.Model):
    class Warrany_Type(models.TextChoices):
        manufacturer = 1, 'manufacturer\'s warranty'
        extended = 2, 'extended warranty'

    period_in_months = models.IntegerField()
    type = models.CharField(max_length=1, choices=Warrany_Type.choices)
    coverage_details = models.TextField()
    exclusions = models.TextField()
    cusomer_service_phone_number = models.CharField(max_length=15)
    start_date = models.DateField()
    def __str__(self) -> str:
        return str(self.start_date)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    qunatity = models.PositiveIntegerField()
    weight = models.FloatField()
    warranty = models.OneToOneField(Warranty, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    class Payment_Method(models.TextChoices):
        card = 1, 'card'
        cash = 2, 'cash'
    date = models.DateField()
    shipping_address = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=1, choices=Payment_Method.choices)
    order_total = models.IntegerField()
    products = models.ManyToManyField(Product, symmetrical=False) 
    def __str__(self) -> str:
        return self.shipping_address

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    birth_date = models.DateField()
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.last_name

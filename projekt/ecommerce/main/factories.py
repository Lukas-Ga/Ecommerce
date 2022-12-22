import random
import factory
from factory.django import DjangoModelFactory
from .models import *
import re

class WarrantyFactory(DjangoModelFactory):
    class Meta:
        model = Warranty
    
    period_in_months = factory.Faker('random_int', min=12, max=120)
    type = factory.Faker('random_element', elements=Warranty.Warrany_Type.choices)
    coverage_details = factory.Faker('text')
    exclusions = factory.Faker('text')
    cusomer_service_phone_number = factory.Faker('phone_number')
    start_date = factory.Faker('date_time')

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('first_name')
    description = factory.Faker('text')
    price = factory.Faker('random_int', min=0, max=32767)
    qunatity = factory.Faker('random_int', min=0, max=2147483647)
    weight = factory.Faker('random_int', min=0, max=100)
    warranty = factory.SubFactory(WarrantyFactory)

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
    date = factory.Faker('date_time')
    shipping_address = factory.Faker('address')
    payment_method = factory.Faker('random_element', elements=Order.Payment_Method.choices)
    products = factory.RelatedFactoryList(ProductFactory)
    order_total = factory.Faker('random_int')
    
class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone_number = factory.Faker('phone_number')
    address = factory.Faker('address')
    birth_date = factory.Faker('date_time')
    orders = factory.SubFactory(OrderFactory)

import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factories import *

warranties = WarrantyFactory.create_batch(20)
products = ProductFactory.create_batch(20)
orders = OrderFactory.create_batch(10)
customers = CustomerFactory.create_batch(10)

Warranty.objects.bulk_create(warranties)
Product.objects.bulk_create(products)
Order.objects.bulk_create(orders)
Customer.objects.bulk_create(customers)

# from django.core.management.base import BaseCommand

# class Command(BaseCommand):
#     help = 'Setup test data'

#     def handle(self, *args, **options):
#         Warranty.objects.all().delete()
#         Product.objects.all().delete()
#         Order.objects.all().delete()
#         Customer.objects.all().delete()
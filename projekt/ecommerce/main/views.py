from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.
class WarrantyList(ListView):
    model = Warranty

class ProductList(ListView):
    model = Product

class OrderList(ListView):
    model = Order

class CustomerList(ListView):
    model = Customer
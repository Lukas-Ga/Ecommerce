from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('warranties/', WarrantyList.as_view()),
    path('products/', ProductList.as_view()),
    path('orders/', OrderList.as_view()),
    path('customers/', CustomerList.as_view()),
]
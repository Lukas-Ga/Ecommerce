from django.contrib import admin
from .models import *

# Register your models here.
main_models = [Order,Product, Customer, Warranty]
admin.site.register(main_models)

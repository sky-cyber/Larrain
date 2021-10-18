from django.contrib import admin
from PuntoVentas.models import *

# Register your models here.

admin.site.register([Category, ShippingAddress, Orders, Report, Product, Client,
                     Supplier, Dispatch, OderItem, SalesDetail, Contact, Review, User])

from django.contrib import admin
from PuntoVentas.models import *

# Register your models here.

admin.site.register([Category, ShippingAddress, Orders,
                     Product, Supplier, OderItem, Contact,
                     Review, User, Dispatcher,
                     Client, Sale, DetSale, FlatFile])

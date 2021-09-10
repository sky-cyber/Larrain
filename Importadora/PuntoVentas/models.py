from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=200, null=True, blank=True)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", unique=True)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre del Producto", unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default="")
    mark = models.CharField(default="", verbose_name='Marca del Producto',
                            max_length=50, blank=False, null=False)
    description = models.TextField(default="", verbose_name='Descripción', blank=False, null=False)
    marked_price = models.PositiveIntegerField(default=0, max_length=20, verbose_name="Precio De Mercado")
    selling_price = models.PositiveIntegerField(default=0, max_length=20, verbose_name="Precio de Venta")
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="product", null=True, blank=True)
    warranty = models.CharField(max_length=200, default="", null=True, blank=True, verbose_name="Garantia")
    view_count = models.PositiveIntegerField(default=0, verbose_name="Cantidad de Visitas")
    date_create = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    subtotal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Cart: " + str(self.cart.id) + "CartProduct: " + str(self.id)


ORDER_STATUS = (
    ("Orden recivida", "Orden recibida"),
    ("Orden En Proceso", "Orden En Proceso"),
    ("Orden En Camino", "Orden En Camino"),
    ("Orden Completada", "Orden Completada"),
    ("Orden Cancelada", "Orden Cancelada"),
)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, unique=True, verbose_name="Celular")
    email = models.EmailField(max_length=50, unique=True, verbose_name="Correo Electronico")
    subtotal = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    date_create = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return "Order: " + str(self.id)

# class detSales(models.Model):
#     sale = models.ForeignKey('Sales', on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     count = models.IntegerField(default=0)
#     price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#
#     def __str__(self):
#         return self.product.name
#
#     class Meta:
#         verbose_name = "detVenta"
#         verbose_name_plural = "detVentas"
#         ordering = ['id']
#
#
# class Sales(models.Model):
#     client = models.ForeignKey('Client', on_delete=models.CASCADE)
#     date_sale = models.DateTimeField(default=datetime.now, verbose_name="Fecha De Venta")
#     subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#
#     def __str__(self):
#         return self.client.names
#
#     class Meta:
#         verbose_name = "Venta"
#         verbose_name_plural = "Ventas"
#         ordering = ['id']


# class Client(models.Model):
#     names = models.CharField(max_length=150, verbose_name="Nombres")
#     last_name = models.CharField(max_length=150, verbose_name="Apellidos")
#     rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
#     birthday = models.DateField(default=datetime.now, verbose_name="Fecha De Nacimiento")
#     address = models.CharField(max_length=100, null=True, blank=True, verbose_name="Direccion")
#     gender = models.CharField(max_length=50, default="male", verbose_name="Sexo")
#     email = models.EmailField(max_length=50, unique=True, verbose_name="Correo")
#     phone = models.CharField(max_length=12, unique=True, blank=False, null=False, verbose_name="Celular")
#     date_create = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")
#
#     def __str__(self):
#         return "{0},{1}".format(self.last_name, self.names)
#
#     class Meta:
#         verbose_name = "Cliente"
#         verbose_name_plural = "Clientes"
#         ordering = ['names']

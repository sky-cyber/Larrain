from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", unique=True)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']


class Supplier(models.Model):
    rut = models.CharField(max_length=15, verbose_name="Rut", unique=True, blank=False, null=False)
    company = models.CharField(max_length=200, verbose_name="Empresa", blank=False, null=False)
    phone = models.CharField(default="", max_length=12, verbose_name="Celular", unique=True, blank=False, null=False)
    address = models.CharField(default="", max_length=250, verbose_name="Dirección", blank=False, null=False)
    email = models.EmailField(default="", max_length=100, verbose_name="Email", unique=True, blank=False, null=False)
    detailProduct = models.TextField(default="", verbose_name='Descripción', blank=False, null=False)
    timeDelivery = models.CharField(default="", max_length=250, verbose_name="Tiempo de Entrega", blank=False, null=False)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return self.rut

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['id']


class Role(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ['id']


class Users(models.Model):
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=50,verbose_name="Nombre de usuario")
    first_name = models.CharField(max_length=50,verbose_name="Nombres")
    last_name = models.CharField(max_length=200,verbose_name="Apellidos")
    Password = models.CharField(default="", max_length=200, verbose_name="Contraseña")
    email = models.EmailField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['id']


class Product(models.Model):
    user = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="Nombre del Producto", unique=True)
    slug = models.SlugField(unique=True, default="")
    image = models.ImageField(upload_to="product", null=True, blank=True)
    brand = models.CharField(default="", verbose_name='Marca del Producto',
                            max_length=50, blank=False, null=False)
    description = models.TextField(default="", verbose_name='Descripción', blank=False, null=False)
    rating = models.DecimalField(default=0, max_digits=7 , decimal_places=2, blank=True, null=True)
    numReviews = models.PositiveIntegerField(default=0, verbose_name="Cantidad de Visitas")
    salePrice = models.PositiveIntegerField(default=0, verbose_name="Precio")
    offerPrice = models.PositiveIntegerField(default=0, verbose_name="Oferta")
    stock = models.PositiveIntegerField(default=0)
    warranty = models.CharField(max_length=200, default="", null=True, blank=True, verbose_name="Garantia")
    dispachTime = models.CharField(max_length=200, default="", null=True, blank=True, verbose_name="Tiempo de envio")
    statusProduct = models.BooleanField(default="", verbose_name="Estado", null=True, blank=True )
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']


class Contact(models.Model):
    user = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="Cliente")
    claim = models.CharField(max_length=500, verbose_name="Reclamo")
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['name']


class Report(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        ordering = ['id']


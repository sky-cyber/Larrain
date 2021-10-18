from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from Importadora.settings import MEDIA_URL, STATIC_URL


# Create your models here

class User(AbstractUser):
    image = models.ImageField(upload_to='users', null=True, blank=True)
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'admin/img/profile.png')


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
    detailProduct = models.TextField(default="", verbose_name='Detalle de los productos', blank=False, null=False)
    timeDelivery = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha de Entrega(dd/mm/yyyy)", blank=False, null=False)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['id']


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    first_name = models.CharField(max_length=50, verbose_name="Nombres")
    last_name = models.CharField(max_length=200, verbose_name="Apellidos")
    Password = models.CharField(default="", max_length=200, verbose_name="Contraseña")
    email = models.EmailField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['id']


class Product(models.Model):
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

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']


TYPE_CLAIM = (
    ("Consulta", "Consulta"),
    ("Reclamo", "Reclamo"),
    ("Sugerencía", "Sugerencía"),
    ("Felicitaciones", "Felicitaciones"),
)


class Contact(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Cliente")
    phone = models.CharField(default="", max_length=12, verbose_name="Celular", blank=False, null=False)
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name="Correo")
    typeClaim = models.CharField(default="", max_length=100, choices=TYPE_CLAIM)
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


class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(default=0, max_digits=7 , decimal_places=2, blank=True, null=True)
    comments = models.TextField(default="", verbose_name='Descripción', blank=False, null=False)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return str(self.rating)

    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
        ordering = ['id']


ORDER_STATUS = (
    ("Order received", "Orden recibida"),
    ("Order In Process", "Orden En Proceso"),
    ("Order On The Way", "Orden En Camino"),
    ("Order Completed", "Orden Completada"),
    ("Order canceled", "Orden Cancelada"),
)


class Orders(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    paymentMethod = models.CharField(max_length=250, verbose_name="Tipo de pago")
    taxPrice = models.DecimalField(default=0, max_digits=7 , decimal_places=2, blank=True, null=True)
    shippingPrice = models.DecimalField(default=0, max_digits=7 , decimal_places=2, blank=True, null=True)
    totalPrice = models.DecimalField(default=0, max_digits=7 , decimal_places=2, blank=True, null=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=100, choices=ORDER_STATUS)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.get_total_items()
        total = sum([item.get_sub_total for item in orderitems])
        return total

    @property
    def get_total_items(self):
        orderitems = self.get_total_items()
        total = sum([item.qty for item in orderitems])
        return total

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"
        ordering = ['id']


class OderItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey('Orders', on_delete=models.SET_NULL, null=True, blank=True)
    qty = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    image = models.CharField(max_length=100,null=True, blank=True)

    @property
    def get_sub_total(self):
        sub_total = self.product.offerPrice * self.qty
        return sub_total

    @property
    def get_cart_total(self):
        items = OderItem.objects.all()
        total = sum([item.get_sub_total for item in items])
        return total

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Orden de articulo"
        verbose_name_plural = "Ordenes de articulos"
        ordering = ['id']


class ShippingAddress(models.Model):
    order = models.OneToOneField('Orders', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=250, verbose_name="Dirección", null=True, blank=True)
    city = models.CharField(max_length=250, verbose_name="Ciudad", null=True, blank=True)
    postalCode = models.CharField(max_length=100, verbose_name="Ciudad", null=True, blank=True)
    country = models.CharField(max_length=250, verbose_name="Ciudad", null=True, blank=True)
    shippingPrice = models.DecimalField(default=0, max_digits=7 , decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.address)

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
        ordering = ['id']


class SalesDetail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    report = models.ForeignKey('Report', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.OneToOneField('Orders', on_delete=models.CASCADE, null=True, blank=True)
    numDetail = models.IntegerField(default=0, null=True, blank=True)
    paymentMethod = models.CharField(max_length=250, verbose_name="Tipo de pago")
    totalPrice = models.DecimalField(default=0, max_digits=7 , decimal_places=2, blank=True, null=True)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return str(self.numDetail)

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Ventas"
        ordering = ['id']


class Dispatch(models.Model):
    shippingadress = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, null=True, blank=True)
    dispatchNum = models.IntegerField(default=0, null=True, blank=True)
    dispatchDate = models.DateField(auto_now=True, auto_now_add=False)
    destinationCity = models.CharField(max_length=250, verbose_name="Ciudad de destino", null=True, blank=True)
    destinationAddress = models.CharField(max_length=400, verbose_name="Dirección de destino", null=True, blank=True)
    dispatched_By = models.CharField(max_length=400, verbose_name="Despachado por:", null=True, blank=True)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return str(self.destinationCity)

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"
        ordering = ['id']













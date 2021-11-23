from datetime import datetime

from crum import get_current_request
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.forms import model_to_dict

from Importadora.settings import MEDIA_URL, STATIC_URL


# Create your models here

class User(AbstractUser):
    image = models.ImageField(upload_to='users', null=True, blank=True)
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'admin/img/profile.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%m-%d %H:%M:%S')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass


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
    first_name = models.CharField(default="", max_length=50, verbose_name="Primer Nombre")
    second_name = models.CharField(default="", max_length=50, verbose_name="Segundo Nombre")
    pather_last_name = models.CharField(default="", max_length=50, verbose_name="Apellido Paterno")
    mother_last_name = models.CharField(default="", max_length=50, verbose_name="Apellido Materno")
    birthday = models.DateField(default=datetime.now, auto_now=False, auto_now_add=False,
                                verbose_name="Fecha de Nacimiento", blank=False, null=False)
    phone = models.CharField(default="", max_length=9, verbose_name="Celular", unique=True, blank=False, null=False)
    address = models.CharField(default="", max_length=250, verbose_name="Dirección", blank=False, null=False)
    email = models.EmailField(default="", max_length=100, verbose_name="Email", unique=True, blank=False, null=False)
    detailProduct = models.TextField(
        default="Nombre del Producto: \n1)\n2)\n3) \n Cantidad de dichos productos: \n1)\n2)\n3) "
        , verbose_name='Detalle de los productos', blank=False, null=False)
    timeDelivery = models.DateField(default=datetime.now, auto_now=False,
                                    auto_now_add=False, verbose_name="Fecha de Entrega de los Productos",
                                    blank=False, null=False)
    image = models.ImageField(upload_to='supplier', null=True, blank=True)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'admin/img/profile.png')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['id']


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="Nombre del Producto", unique=True)
    slug = models.SlugField(unique=True, default="")
    image = models.ImageField(upload_to="product", null=True, blank=True)
    brand = models.CharField(default="", verbose_name='Marca del Producto', max_length=50, blank=False, null=False)
    description = models.TextField(default="", verbose_name='Descripción', blank=False, null=False)
    rating = models.DecimalField(default=0, max_digits=7, decimal_places=2, blank=True, null=True)
    numReviews = models.PositiveIntegerField(default=0, verbose_name="Cantidad de Visitas")
    salePrice = models.PositiveIntegerField(default=0, verbose_name="Precio")
    offerPrice = models.PositiveIntegerField(default=0, verbose_name="Oferta")
    offer = models.BooleanField(default="False", verbose_name="Producto En Oferta", null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    warranty = models.CharField(max_length=200, default="", null=True, blank=True, verbose_name="Garantia")
    dispachTime = models.CharField(max_length=200, default="", null=True, blank=True, verbose_name="Tiempo de envio")
    statusProduct = models.BooleanField(default="False", verbose_name="Estado", null=True, blank=True)
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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
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


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(default=0, max_digits=7, decimal_places=2, blank=True, null=True)
    comments = models.TextField(default="", verbose_name='Descripción', blank=False, null=False)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return str(self.rating)

    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
        ordering = ['id']


ORDER_STATUS = (
    ("Orden A Despacho", "Orden A Despacho"),
    ("Orden En Proceso", "Orden En Proceso"),
    ("Orden En Camino", "Orden En Camino"),
    ("Orden Completada", "Orden Completada"),
    ("Orden Cancelada", "Orden Cancelada"),
)


class Dispatcher(models.Model):
    rut = models.CharField(max_length=13, unique=True, verbose_name="Rut", null=True, blank=False)
    first_name = models.CharField(max_length=100, verbose_name="Nombre del Cliente", null=True, blank=False)
    second_name = models.CharField(max_length=100, verbose_name="Segundo Nombre", null=True, blank=False)
    pather_last_name = models.CharField(default="", max_length=100, verbose_name="Apellido Paterno", null=True,
                                        blank=False)
    mother_last_name = models.CharField(default="", max_length=100, verbose_name="Apellido Materno", null=True,
                                        blank=False)
    phone = models.CharField(default="", max_length=9, unique=True, verbose_name="Celular", null=True, blank=False)
    email = models.EmailField(default="", max_length=50, unique=True,
                              verbose_name="Correo Electronico", null=True, blank=False)
    image = models.ImageField(upload_to='dispatcher', null=True, blank=True)
    createdAt = models.DateField(auto_now=True, auto_now_add=False,
                                 verbose_name="Fecha de Registro", null=True, blank=False)

    def __str__(self):
        return self.first_name

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'admin/img/profile.png')

    class Meta:
        verbose_name = "Despachador"
        verbose_name_plural = "Despachadores"
        ordering = ['id']


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    dispatcher = models.ForeignKey(Dispatcher, on_delete=models.SET_NULL, null=True, blank=True)
    paymentMethod = models.CharField(max_length=250, verbose_name="Tipo de pago")
    shippingValue = models.PositiveIntegerField(default=0, verbose_name="Precio De Envio")
    shippingPrice = models.PositiveIntegerField(default=0, verbose_name="SubTotal")
    totalPrice = models.PositiveIntegerField(default=0, verbose_name="Total")
    isPaid = models.BooleanField(default=False, null=True, blank=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False, null=True, blank=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=100, choices=ORDER_STATUS)
    arrivalDate = models.DateField(default=datetime.now, auto_now=False,
                                   auto_now_add=False, verbose_name="Fecha de Llegada de los Productos",
                                   blank=True, null=True)
    createdAt = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return str(self.id)

    @property
    def tax(self):
        self.shippingValue = 0
        totalValue = self.shippingPrice * int(self.shippingValue)
        return totalValue

    @property
    def total(self):
        self.totalPrice = self.shippingPrice + self.tax
        return self.totalPrice

    @property
    def shipping(self):
        shipping = False
        orderitems = self.oderitem_set.all()
        for i in orderitems:
            if i.product.statusProduct == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        items = self.oderitem_set.all()
        total = sum([item.get_sub_total for item in items])
        return total

    @property
    def get_cart_items(self):
        items = self.oderitem_set.all()
        total = sum([item.qty for item in items])
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

    @property
    def get_sub_total(self):
        if self.product.offer == True:
            sub_total = self.product.offerPrice * self.qty
        else:
            sub_total = self.product.salePrice * self.qty
        return sub_total

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Orden de articulo"
        verbose_name_plural = "Ordenes de articulos"
        ordering = ['id']


class ShippingAddress(models.Model):
    order = models.OneToOneField('Orders', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(default="", max_length=250, verbose_name="Dirección", null=True, blank=True)
    city = models.CharField(default="", max_length=250, verbose_name="Ciudad", null=True, blank=True)
    postalCode = models.CharField(default="", max_length=100, verbose_name="Codigo Postal", null=True, blank=True)
    country = models.CharField(default="", max_length=250, verbose_name="País", null=True, blank=True)

    def __str__(self):
        return str(self.address)

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
        ordering = ['id']


GENDER = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Prefiero No Decir", "Prefiero No Decir"),
)


class Client(models.Model):
    rut = models.CharField(max_length=13, unique=True, verbose_name="Rut", null=True, blank=False)
    first_name = models.CharField(max_length=100, verbose_name="Primer Nombre", null=True, blank=False)
    second_name = models.CharField(max_length=100, verbose_name="Segundo Nombre", null=True, blank=False)
    pather_last_name = models.CharField(default="", max_length=100, verbose_name="Apellido Paterno", null=True,
                                        blank=False)
    mother_last_name = models.CharField(default="", max_length=100, verbose_name="Apellido Materno", null=True,
                                        blank=False)
    birthday = models.DateField(default=datetime.now, verbose_name="Fecha de Nacimiento", auto_now=False,
                                auto_now_add=False, null=False, blank=False)
    phone = models.CharField(default="", max_length=9, unique=True, verbose_name="Celular", null=True, blank=False)
    email = models.EmailField(default="", max_length=50, unique=True,
                              verbose_name="Correo Electronico", null=True, blank=False)
    gender = models.CharField(default="", max_length=50, choices=GENDER)
    address = models.CharField(default="", max_length=250, verbose_name="Dirección", null=True, blank=True)
    city = models.CharField(default="", max_length=250, verbose_name="Ciudad", null=True, blank=True)
    createdAt = models.DateField(auto_now=True, auto_now_add=False,
                                 verbose_name="Fecha de Registro", null=True, blank=True)

    def __str__(self):
        return self.first_name

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['date_birthday'] = self.birthday.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['id']


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=False)
    value = models.PositiveIntegerField(default=0, verbose_name="Precio De Envio", null=True, blank=True)
    subtotal = models.PositiveIntegerField(default=0, verbose_name="SubTotal", null=True, blank=True)
    total = models.PositiveIntegerField(default=0, verbose_name="Total", null=True, blank=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.client.first_name

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    price = models.PositiveIntegerField(default=0, verbose_name="Precio", null=True, blank=True)
    qty = models.PositiveIntegerField(default=0, verbose_name="Cantidad", null=True, blank=True)
    subtotal = models.PositiveIntegerField(default=0, verbose_name="SubTotal", null=True, blank=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalle de Ventas"
        ordering = ['id']

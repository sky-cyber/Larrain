import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import render_to_string
from django.utils import timezone

from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from Importadora import settings
from PuntoVentas.models import *
import json


# class AddToCartView(TemplateView):
#     template_name = 'Cart/addtocart.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # get product id from requested url
#         product_id = self.kwargs['prod_id']
#         # get product
#         product_obj = Product.objects.get(id=product_id)
#         # check if card exists
#         cart_id = self.request.session.get('card_id', None)
#         try:
#             if cart_id:
#                 cart_obj = Cart.objects.get(id=cart_id)
#                 this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)
#                 # item already exists in cart
#                 if this_product_in_cart.exists():
#                     cartproduct = this_product_in_cart.last()
#                     cartproduct.quantity += 1
#                     cartproduct.subtotal += product_obj.selling_price
#                     cartproduct.save()
#                     cart_obj.total += product_obj.selling_price
#                     cart_obj.save()
#                     print("Carro se sumaron valores del mismo producto")
#                     # new item is added in cart
#                 else:
#                     cartproduct = CartProduct.objects.create(cart=cart_obj, product=product_obj,
#                                                              rate=product_obj.selling_price,
#                                                              quantity=1, subtotal=product_obj.selling_price)
#                     cart_obj.total += product_obj.selling_price
#                     cart_obj.save()
#                     print("Se agregaron nuevos productos")
#             else:
#                 cart_obj = Cart.objects.create(total=0)
#                 self.request.session['card_id'] = cart_obj.id
#                 cartproduct = CartProduct.objects.create(cart=cart_obj, product=product_obj,
#                                                          rate=product_obj.selling_price,
#                                                          quantity=1, subtotal=product_obj.selling_price)
#                 cart_obj.total += product_obj.selling_price
#                 cart_obj.save()
#                 print("Carro nuevo")
#             return context
#         except:
#             pass
def Mycart(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
        items = order.oderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    context = {'items': items, 'order': order, 'category': category}
    return render(request, 'Cart/mycart.html', context)


def Checkout(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
        items = order.oderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    context = {'items': items, 'order': order, 'category': category}
    return render(request, 'Cart/checkout.html', context)


def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
    orderItem, created = OderItem.objects.get_or_create(order=order, product=product)

    if orderItem.qty < orderItem.product.stock:
        if action == 'add':
            orderItem.qty = (orderItem.qty + 1)
        elif action == 'remove':
            orderItem.qty = (orderItem.qty - 1)
        orderItem.save()
    elif action == 'remove':
        orderItem.qty = (orderItem.qty - 1)
        orderItem.save()

    if orderItem.qty <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def ProcessOrder(request):
    transaction_id = datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        user = request.user
        order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
        subtotal = data['form']['subtotal']
        order.transaction_id = transaction_id
        order.shippingPrice = subtotal
        order.paidAt = timezone.now()
        order.isPaid = True
        order.isDelivered = True
        order.paymentMethod = "PayPal"
        order.status = 'Orden En Proceso'
        order.deliveredAt = timezone.now()
        order.totalPrice = order.shippingPrice

        order.save()

        user.save()

        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        mailServer.starttls()
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

        email_to = user.email

        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Detalle de la Orden"

        content = render_to_string('Email/DetailOrder.html', {
            'user': user,
            'order': order,
            'items': order.oderitem_set.all()
        })
        # Adjuntamos el texto
        mensaje.attach(MIMEText(content, 'html'))

        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                            email_to,
                            mensaje.as_string())

        if order.shipping == True:
            ShippingAddress.objects.create(
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                country=data['shipping']['country'],
                postalCode=data['shipping']['postalCode'],
            )

        # productId = data['productId']
        # product = Product.objects.get(pk=productId)
        # orderItem , created = OderItem.objects.get_or_create(order=order, product=product)
        #
        # orderItem.qty -= orderItem.product.stock
        # orderItem.product.save()

    else:
        print('user not authenticated')

    return JsonResponse('payment complete!', safe=False)

from django.views.generic import TemplateView
from django.shortcuts import render

from PuntoVentas.models import *
from django.contrib.auth.models import User


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
#
#
def mycart(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Orders.objects.get_or_create(client=client, isPaid=False, isDelivered=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items}
    return render(request, 'Cart/mycart1.html', context)


class AllitemsView(TemplateView):
    model = Orders
    template_name = 'Cart/mycart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = OderItem.objects.all()
        context['button'] = 'Agregar al Carrito'
        context['button1'] = 'Ver Producto'
        return context

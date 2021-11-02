from django.shortcuts import render
from PuntoVentas.models import *


def Profile(request):
    if request.user.is_authenticated:
        user = request.user
        order = Orders.objects.filter(user=user)
    else:
        order = []
    context = {'order': order}
    return render(request, 'Profile/profile.html', context)


def OrderDetail(request, pk):
    if request.user.is_authenticated:
        user = request.user
        order = Orders.objects.get(user=user, id=pk)
        items = order.oderitem_set.all()
        #shipping = order.shippingaddress_set.all()
    else:
        order = []
        items = []
        #shipping = []
    context = {'order': order, 'items': items} #'shipping': shipping
    return render(request, 'Profile/orderDetail.html', context)






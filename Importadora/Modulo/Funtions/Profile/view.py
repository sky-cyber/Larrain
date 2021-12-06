from django.shortcuts import render, redirect
from PuntoVentas.models import *
from django.core.paginator import Paginator
from Modulo.Funtions.Profile.form import ProfileUpdateForm


def Profile(request):
    if request.user.is_authenticated:
        user = request.user
        order = Orders.objects.filter(user=user).order_by("-id")
        paginator = Paginator(order, 7)
        page = request.GET.get('page') or 1
        order = paginator.get_page(page)
        current_page = int(page)
        pages = range(1, order.paginator.num_pages + 1)
    else:
        order = []
        pages = ""
        current_page = ""
    context = {'order': order, 'pages': pages, 'current_page': current_page}
    return render(request, 'Profile/profile.html', context)


def OrderDetail(request, pk):
    button = "Volver"
    PDF = "Generar PDF"
    if request.user.is_authenticated:
        PDF = "Generar PDF"
        user = request.user
        order = Orders.objects.get(user=user, id=pk)
        items = order.oderitem_set.all()
        if ShippingAddress.objects.filter(order=order).exists():
            shipping = ShippingAddress.objects.get(order=order)
        else:
            shipping = []
    else:
        order = []
        items = []
        shipping = []
    context = {'order': order, 'items': items, 'shipping': shipping,
               'button': button, 'PDF': PDF}
    return render(request, 'Profile/orderDetail.html', context)


def UpdateProfile(request):

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'Profile/updateProfile.html', context)


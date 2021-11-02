from django.urls import path

from Modulo.Funtions.cart.view import Mycart, Checkout, UpdateItem, ProcessOrder
from PuntoVentas.views import home, team, CatalogueListView, AllCategoriesView, ProductDetailView
from Modulo.Funtions.claim.view import ContactCreateView
from Modulo.Funtions.Email.view import WelcomeView
from Modulo.Funtions.Profile.view import Profile, OrderDetail
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # URL THE WEB
    path('', home, name='home'),
    path('catalogo/', CatalogueListView.as_view(), name='catalogue'),
    path('team/', team, name='team'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('allcategory/', AllCategoriesView.as_view(), name='all_categories'),
    path('producto/<slug:slug>/', ProductDetailView.as_view(), name='productDetail'),

    # URL THE CART
    path('mi-carrito/', Mycart, name='mycart'),
    path('checkout/', Checkout, name='checkout'),
    path('update_item/', login_required(UpdateItem), name='update-item'),
    path('process_order/', ProcessOrder, name='process-order'),

    # URL SEND EMAIL
    path('welcome/', WelcomeView.as_view(), name='welcome'),

    # URL profile
    path('profile/', login_required(Profile), name='profile'),
    path('order/detail/<int:pk>/', OrderDetail, name='order-detail')

]

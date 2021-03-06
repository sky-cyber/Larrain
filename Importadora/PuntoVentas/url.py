from django.urls import path

from Modulo.Funtions.cart.view import Mycart, Checkout, UpdateItem, ProcessOrder
from PuntoVentas.views import *
from Modulo.Funtions.claim.view import ContactCreateView
from Modulo.Funtions.Email.view import WelcomeView
from Modulo.Funtions.Profile.view import Profile, OrderDetail, UpdateProfile
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # URL THE WEB
    path('', home, name='home'),
    path('catalogo/', Catalogue, name='catalogue'),
    path('team/', team, name='team'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('allcategory/', AllCategoriesView.as_view(), name='all_categories'),
    path('producto/<slug:slug>/', ProductDetailView.as_view(), name='productDetail'),
    path('category/<slug:slug>/', TypeCategory.as_view(), name='type_category'),
    path('product/offer/', login_required(ProductOffer), name='product_offer'),

    # URL THE CART
    path('mi-carrito/', Mycart, name='mycart'),
    path('checkout/', login_required(Checkout), name='checkout'),
    path('update_item/', login_required(UpdateItem), name='update-item'),
    path('process_order/', ProcessOrder, name='process-order'),

    # URL SEND EMAIL
    path('welcome/', WelcomeView.as_view(), name='welcome'),

    # URL profile
    path('profile/', login_required(Profile), name='profile'),
    path('order/detail/<int:pk>/', OrderDetail, name='order-detail'),
    path('update/profile', login_required(UpdateProfile), name="update_profile"),

    # URL PURCHASE DETAIL
    path('purchase/detail/', PurchaseDetail.as_view(), name='purchase_detail')
]

from django.urls import path

from Modulo.Funtions.cart.view import mycart
from PuntoVentas.views import home, team, CatalogueListView, AllCategoriesView, ProductDetailView
from Modulo.Funtions.claim.view import ContactCreateView
from Modulo.Funtions.Email.view import WelcomeView

urlpatterns = [

    # URL THE WEB
    path('', home, name='home'),
    path('catalogo/', CatalogueListView.as_view(), name='catalogue'),
    path('team/', team, name='team'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('allcategory/', AllCategoriesView.as_view(), name='all_categories'),
    path('producto/<slug:slug>/', ProductDetailView.as_view(), name='productDetail'),

    # URL THE CART
    path('mi-carrito/', mycart, name='mycart'),

    # URL SEND EMAIL
    path('welcome/', WelcomeView.as_view(), name='welcome'),

]

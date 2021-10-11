from django.urls import path

from Modulo.Funtions.cart.view import AllitemsView,mycart
from PuntoVentas.views import home, team, CatalogueListView, AllCategoriesView, ProductDetailView
from Modulo.Funtions.claim.view import RegisterCreateView

urlpatterns = [

    # URL THE WEB
    path('', home, name='home'),
    path('catalogo/', CatalogueListView.as_view(), name='catalogue'),
    path('team/', team, name='team'),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('allcategory/', AllCategoriesView.as_view(), name='all_categories'),
    path('producto/<slug:slug>/', ProductDetailView.as_view(), name='productDetail'),

    # URL THE CART
    path('mi-carrito/', mycart, name='mycart'),
    path('allitem', AllitemsView.as_view(), name='allitem')

]

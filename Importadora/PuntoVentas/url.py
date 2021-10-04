from django.urls import path

# from Modulo.Funtions.cart.view import AddToCartView, MyCartView
from PuntoVentas.views import home, team, register, CatalogueListView, AllCategoriesView, ProductDetailView

urlpatterns = [

    # URL THE WEB
    path('', home, name='home'),
    path('catalogo/', CatalogueListView.as_view(), name='catalogue'),
    path('equipo/', team, name='team'),
    path('registro/', register, name='register'),
    path('todas-categorias/', AllCategoriesView.as_view(), name='all_categories'),
    path('producto/<slug:slug>/', ProductDetailView.as_view(), name='productDetail'),

    # URL THE CART
    # path('add-to-cart/<int:prod_id>/', AddToCartView.as_view(), name='addtocart'),
    # path('mi-carrito/', MyCartView.as_view(), name='mycart')

]
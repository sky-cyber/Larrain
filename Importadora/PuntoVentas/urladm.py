from django.urls import path

from Modulo.Funtions.category.view import *
from Modulo.Funtions.product.view import *
from PuntoVentas.views import adm

urlpatterns = [

    # URL THE PANEL
    path('', adm, name='adm'),

    # URL OF CATEGORY
    path('category/list', CategoryListView.as_view(), name='category_list'),
    path('category/add', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    # URL THE PRODUCT
    path('product/add', ProductCreateView.as_view(), name='product_create'),
    path('product/list', ProductListView.as_view(), name='product_list'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]

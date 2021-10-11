from django.urls import path

from Modulo.Funtions.category.view import *
from Modulo.Funtions.product.view import *
from Modulo.Funtions.supplier.view import *
from Modulo.Funtions.claim.view import *
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
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # URL THE SUPPLIER
    path('supplier/add', SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/list', SupplierListView.as_view(), name='supplier_list'),
    path('supplier/edit/<int:pk>/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', SupplierDeleteView.as_view(), name='supplier_delete'),

    # URL THE CLAIM
    path('claim/list', ClaimListView.as_view(), name='claim_list'),
    path('claim/delete/<int:pk>/', ClaimDeleteView.as_view(), name='claim_delete')

]

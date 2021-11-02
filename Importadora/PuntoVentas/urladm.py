from django.urls import path

from Modulo.Funtions.category.view import *
from Modulo.Funtions.product.view import *
from Modulo.Funtions.security.view import *
from Modulo.Funtions.supplier.view import *
from Modulo.Funtions.claim.view import *
from Modulo.Funtions.PDF.view import *
from Modulo.Funtions.Order.view import *
from PuntoVentas.views import DashboardView, PerfilView
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # URL FOR DASHBOARD
    path('', login_required(DashboardView.as_view()), name='adm'),

    # URL FOR PERFIL
    path('perfil/', login_required(PerfilView.as_view()), name='perfil'),

    # URL OF CATEGORY
    path('category/list', login_required(CategoryListView.as_view()), name='category_list'),
    path('category/add', login_required(CategoryCreateView.as_view()), name='category_create'),
    path('category/edit/<int:pk>/', login_required(CategoryUpdateView.as_view()), name='category_update'),
    path('category/delete/<int:pk>/', login_required(CategoryDeleteView.as_view()), name='category_delete'),

    # URL THE PRODUCT
    path('product/add', login_required(ProductCreateView.as_view()), name='product_create'),
    path('product/list', login_required(ProductListView.as_view()), name='product_list'),
    path('product/edit/<int:pk>/', login_required(ProductUpdateView.as_view()), name='product_edit'),
    path('product/delete/<int:pk>/', login_required(ProductDeleteView.as_view()), name='product_delete'),

    # URL THE SUPPLIER
    path('supplier/add', login_required(SupplierCreateView.as_view()), name='supplier_create'),
    path('supplier/list', login_required(SupplierListView.as_view()), name='supplier_list'),
    path('supplier/edit/<int:pk>/', login_required(SupplierUpdateView.as_view()), name='supplier_update'),
    path('supplier/delete/<int:pk>/', login_required(SupplierDeleteView.as_view()), name='supplier_delete'),

    # URL THE CLAIM
    path('claim/list', login_required(ClaimListView.as_view()), name='claim_list'),
    path('claim/delete/<int:pk>/', login_required(ClaimDeleteView.as_view()), name='claim_delete'),

    # URL THE USER
    path('registerUser/', login_required(RegisterUserAdmin), name='registerUser'),
    path('listUser/', login_required(UserListView.as_view()), name='list_user'),

    # URL FOR PDF
    path('product/pdf', ProductPdfView.as_view(), name='product_pdf'),
    path('supplier/pdf', SupplierPdfView.as_view(), name='supplier_pdf'),

    # URL FOR ORDER
    path('order/list/', login_required(OrderListView.as_view()), name='order_list')

]

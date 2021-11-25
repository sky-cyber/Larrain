from django.urls import path

from Modulo.Funtions.category.view import *
from Modulo.Funtions.product.view import *
from Modulo.Funtions.security.view import *
from Modulo.Funtions.supplier.view import *
from Modulo.Funtions.claim.view import *
from Modulo.Funtions.PDF.view import *
from Modulo.Funtions.Order.view import *
from Modulo.Funtions.Sales.view import *
from Modulo.Funtions.Dispatch.view import *
from PuntoVentas.views import DashboardView, PerfilView
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # URL FOR DASHBOARD
    path('', DashboardView.as_view(), name='adm'),

    # URL FOR PERFIL
    path('perfil/', login_required(PerfilView.as_view()), name='perfil'),

    # URL OF CATEGORY
    path('category/list', (CategoryListView.as_view()), name='category_list'),
    path('category/add', (CategoryCreateView.as_view()), name='category_create'),
    path('category/edit/<int:pk>/', (CategoryUpdateView.as_view()), name='category_update'),
    path('category/delete/<int:pk>/', (CategoryDeleteView.as_view()), name='category_delete'),

    # URL THE PRODUCT
    path('product/add', (ProductCreateView.as_view()), name='product_create'),
    path('product/list', (ProductListView.as_view()), name='product_list'),
    path('product/edit/<int:pk>/', (ProductUpdateView.as_view()), name='product_edit'),
    path('product/delete/<int:pk>/', (ProductDeleteView.as_view()), name='product_delete'),
    path('product/list/offer', (ProductListOfferView.as_view()), name='product_list_offer'),
    path('detail/product/<int:pk>/', DetailProduct.as_view(), name='detail_product'),

    # URL THE SUPPLIER
    path('supplier/add', (SupplierCreateView.as_view()), name='supplier_create'),
    path('supplier/list', (SupplierListView.as_view()), name='supplier_list'),
    path('supplier/edit/<int:pk>/', (SupplierUpdateView.as_view()), name='supplier_update'),
    path('supplier/delete/<int:pk>/', (SupplierDeleteView.as_view()), name='supplier_delete'),
    path('contract/supplier/<int:pk>/', (ContractSupplier.as_view()), name='supplier_contract'),

    # URL THE CLAIM
    path('claim/list', (ClaimListView.as_view()), name='claim_list'),
    path('claim/delete/<int:pk>/', (ClaimDeleteView.as_view()), name='claim_delete'),

    # URL THE USER
    path('registerUser/', login_required(RegisterUserAdmin), name='registerUser'),
    path('listUser/', login_required(UserListView.as_view()), name='list_user'),
    path('listClient/', login_required(ClientListView.as_view()), name='list_client'),
    path('updateUser/<int:pk>/', login_required(UpdateUserAdmin), name='updateUser'),
    path('deleteUser/<int:pk>/', login_required(DeleteUserAdmin.as_view()), name='deleteUser'),
    path('change/user/<int:pk>/', ChangeUser.as_view(), name='change_user'),

    # URL FOR PDF
    path('product/pdf', ProductPdfView.as_view(), name='product_pdf'),
    path('supplier/pdf', SupplierPdfView.as_view(), name='supplier_pdf'),
    path('orderDetail/pdf/<int:pk>/', OrderPdfView.as_view(), name='order_pdf'),
    path('contract/pdf/<int:pk>/', ContractpdfView.as_view(), name='contract_pdf'),
    path('dispatch/pdf/', DispatchPdfView.as_view(), name='dispatch_pdf'),

    # URL FOR ORDER
    path('order/all/list/', (OrderListView.as_view()), name='order_list'),
    path('order/complete/', OrderComplete.as_view(), name='order_complete'),
    path('order/inProcess/', OrderInProcess.as_view(), name='order_in_process'),
    path('order/ToDispatch/', OrderToDispatch.as_view(), name='order_to_dispatch'),
    path('order/canceled/', OrderCanceled.as_view(), name='order_canceled'),
    path('order/ontheWay/', OrderOnTheWay.as_view(), name='order_on_the_way'),
    path('orderDetailAdmin/<int:pk>', OrderClientDetail.as_view(), name='order_client_detail'),
    path('change/order/<int:pk>/', ChangeOrderView.as_view(), name='change_order'),

    # URL FOR DISPATCH
    path('dispatch/list/', DispatchList.as_view(), name='dispatch_list'),
    path('detailClient/<int:pk>', DetailClient.as_view(), name='detail_client'),
    path('change/list/dispatch/<int:pk>/', ChangedispatchView.as_view(), name='change_list_dispatch'),
    path('dispatch/list/complete', DispatchListComplete.as_view(), name='dispatch_list_complete'),
    path('dispatch/InTheWay', DispatchListInTheWay.as_view(), name='dispatch_list_InTheWay'),

    # URL FOR DISPATCHER
    path('create/dispatcher', CreateDispatcher.as_view(), name='create_dispatcher'),
    path('list/dispatcher', ListDispacher.as_view(), name='list_dispatcher'),
    path('update/dispatcher/<int:pk>/', UpdateDispatcher.as_view(), name='update_dispatcher'),
    path('delete/dispatcher/<int:pk>/', DeleteDispatcher.as_view(), name='delete_dispatcher'),
    path('detail/dispatcher/<int:pk>/', DetailDispatcher.as_view(), name='detail_dispatcher'),

    # URL FOR CLIENT
    path('create/client', CreateClient.as_view(), name='create_client'),
    path('list/Client/face-to-face', ListClientFaceToFace.as_view(), name='list_client_face'),
    path('edit/Client/<int:pk>/', UpdateClient.as_view(), name='update_client'),
    path('delete/client/<int:pk>/', DeleteClient.as_view(), name='delete_client'),
    path('detail/client/office/<int:pk>/', DetailClientOffice.as_view(), name='detail_client_office'),

    # URL FOR SALE
    path('sale/client', SaleClient.as_view(), name='sale_client')

]

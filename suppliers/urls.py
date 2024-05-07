from django.urls import path

from suppliers.apps import SuppliersConfig
from suppliers.views import SupplierCreateAPIView, SupplierListAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, \
    SupplierDestroyAPIView

app_name = SuppliersConfig.name

urlpatterns = [
    path('supplier/create/', SupplierCreateAPIView.as_view(), name='supplier-create'),
    path('suppliers/', SupplierListAPIView.as_view(), name='supplier-list'),
    path('supplier/<int:pk>/profile/', SupplierRetrieveAPIView.as_view(), name='supplier-profile'),
    path('supplier/<int:pk>/update/', SupplierUpdateAPIView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete/', SupplierDestroyAPIView.as_view(), name='supplier-delete'),
]

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from suppliers.models import Supplier
from suppliers.permissions import IsActive
from suppliers.serializers import SupplierSerializer, SupplierAndProductsSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания поставщика"""
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]


class SupplierListAPIView(generics.ListAPIView):
    """Эндпоинт для отображения всех поставщиков и их продуктов"""
    serializer_class = SupplierAndProductsSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт для отображения поставщика и его продуктов"""
    serializer_class = SupplierAndProductsSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт для обновления поставщика"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт для удаления поставщика"""
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]

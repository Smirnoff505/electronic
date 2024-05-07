from rest_framework import serializers

from suppliers.models import Supplier, Product
from suppliers.validators import ParentValidator


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['debt']
        validators = [ParentValidator(field_level='level', field_parent='parent')]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'model', 'release_date',)


class SupplierAndProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer('products', many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = '__all__'

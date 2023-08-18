from rest_framework import serializers
from apps.products.models import Cart
from apps.products.api.serializers.product_serializers import ProductSerializer, ProductCartSerializer


class CartBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {field_name: {'required': False} for field_name in model._meta.fields}


class CartCreateSerializer(CartBaseSerializer):
    product_id = serializers.CharField(required=True)


class CartUpdateSerializer(CartBaseSerializer):
    pass


class CartDeleteSerializer(CartBaseSerializer):
    pass


class CartSerializer(CartBaseSerializer):
    product = ProductCartSerializer(source='product_set', many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['product', 'product_quantity', 'total_price']

    def get_total_price(self, obj):
        products = obj.product_set.all()
        total = sum(product.price or 0 for product in products)
        return total

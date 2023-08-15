from rest_framework import serializers
from apps.products.models import Product
from django.utils import timezone


class ProductBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {field_name: {'required': False} for field_name in model._meta.fields}


class ProductCreateSerializer(ProductBaseSerializer):
    product_name = serializers.CharField(required=True)
    brand = serializers.CharField(required=True)
    product_type_id = serializers.CharField(required=True)
    main_color = serializers.CharField(required=True)
    logo_color = serializers.CharField(required=True)
    size = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = Product
        fields = [
            'product_name',
            'brand',
            'product_type_id',
            'main_color',
            'logo_color',
            'size',
            'created_at'
        ]


class ProductUpdateSerializer(ProductBaseSerializer):
    updated_at = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = Product
        fields = ['updated_at']


class ProductSerializer(ProductBaseSerializer):
    pass

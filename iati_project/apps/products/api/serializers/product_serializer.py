from rest_framework import serializers
from django.utils import timezone
from apps.products.models import Product, Color


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
    materials = serializers.ListField(child=serializers.IntegerField())


class ProductUpdateSerializer(ProductBaseSerializer):
    pass


class ProductDeleteSerializer(ProductBaseSerializer):
    deleted_at = serializers.DateTimeField(default=timezone.now())


class ProductCartSerializer(ProductBaseSerializer):

    def to_representation(self, instance):
        return {
            'product_id': instance.id,
            'description': instance.description,
            'price': instance.price,
            'url': instance.photo_url
        }


class ProductSerializer(ProductBaseSerializer):
    current_stock = serializers.SerializerMethodField()
    material_composition = serializers.SerializerMethodField()
    main_color = serializers.SerializerMethodField()
    secondary_colors = serializers.SerializerMethodField()
    logo_color = serializers.SerializerMethodField()

    def get_logo_color(self, obj):
        color_id = obj.main_color
        color = Color.objects.get(id=color_id)
        return color.color_name

    def get_main_color(self, obj):
        color_id = obj.main_color
        color = Color.objects.get(id=color_id)
        return color.color_name

    def get_secondary_colors(self, obj):
        color_ids = obj.secondary_colors
        colors = Color.objects.filter(id__in=color_ids)
        return [color.color_name for color in colors]

    def get_material_composition(self, obj):
        materials = obj.compositionmaterial_set.all()
        return [material.material.material_name for material in materials]

    def get_current_stock(self, obj):
        last_stock = obj.stock_set.last()
        return last_stock.current_stock if last_stock else None

    def to_representation(self, instance):
        exclude_fields = []

        if instance.product_type_id == "G0001":  # If product_type_id is Cap
            exclude_fields = [
                'size',
                'sizing_type',
                'has_sleeves',
                'materials',
                'cart',
                'material_composition',
                'materials',
                'deleted_at',
                'update_at'
            ]
        elif instance.product_type_id == "T0002":
            exclude_fields = [
                'logo_color',
                'cart',
                'materials',
                'deleted_at',
                'update_at'
            ]

        representation = super().to_representation(instance)

        for field_name in exclude_fields:
            representation.pop(field_name, None)

        return representation

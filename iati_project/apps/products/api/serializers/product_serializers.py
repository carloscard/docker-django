from rest_framework import serializers
from apps.products.models import Product
from django.utils import timezone


class ProductBaseSerializer(serializers.ModelSerializer):
    #actual_stock = serializers.CharField(source='path-field-from-another-model', required=False)

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('state', 'created_at', 'updated_at')
        extra_kwargs = {field_name: {'required': False} for field_name in model._meta.fields}

        """ 
        ### With this function, we can return the desired display fields. Personally, I believe it's better for
            product scalability that all these filters are done through database queries. This way, there's no need
            to modify code for new features (Open-Closed Principle). #####
            
        def to_representation(self,instance):
            return {
                'id': instance.id,
                'product_name': instance.product_name
                .
                .
                .
            }
        """


class ProductCreateSerializer(ProductBaseSerializer):
    product_name = serializers.CharField(required=True)
    brand = serializers.CharField(required=True)
    product_type_id = serializers.CharField(required=True)
    main_color = serializers.CharField(required=True)
    logo_color = serializers.CharField(required=True)
    size = serializers.CharField(required=True)


class ProductUpdateSerializer(ProductBaseSerializer):
    updated_at = serializers.DateTimeField(default=timezone.now)


class ProductSerializer(ProductBaseSerializer):
    pass

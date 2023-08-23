from rest_framework import serializers
from apps.products.models import Stock


class MaterialBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'
        # exclude = ('state', 'created_at', 'updated_at',)
        extra_kwargs = {field_name: {'required': False} for field_name in model._meta.fields}


class MaterialCreateSerializer(MaterialBaseSerializer):
    pass


class MaterialUpdateSerializer(MaterialBaseSerializer):
    pass


class MaterialDeleteSerializer(MaterialBaseSerializer):
    pass


class MaterialSerializer(MaterialBaseSerializer):
    pass


from rest_framework import serializers
from apps.products.models import CompositionMaterial


class CompositionMaterialBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompositionMaterial
        fields = '__all__'
        # exclude = ('state', 'created_at', 'updated_at',)
        extra_kwargs = {field_name: {'required': False} for field_name in model._meta.fields}


class CompositionMaterialCreateSerializer(CompositionMaterialBaseSerializer):
    pass


class CompositionMaterialUpdateSerializer(CompositionMaterialBaseSerializer):
    pass


class CompositionMaterialDeleteSerializer(CompositionMaterialBaseSerializer):
    pass


class CompositionMaterialSerializer(CompositionMaterialBaseSerializer):
    pass


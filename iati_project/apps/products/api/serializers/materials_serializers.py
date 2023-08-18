from rest_framework import serializers
from apps.products.models import Stock


class StockBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'
        # exclude = ('state', 'created_at', 'updated_at',)
        extra_kwargs = {field_name: {'required': False} for field_name in model._meta.fields}


class StockCreateSerializer(StockBaseSerializer):
    pass


class StockUpdateSerializer(StockBaseSerializer):
    pass


class StockDeleteSerializer(StockBaseSerializer):
    pass


class StockSerializer(StockBaseSerializer):
    pass


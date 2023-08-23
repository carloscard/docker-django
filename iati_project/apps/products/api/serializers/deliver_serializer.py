from rest_framework import serializers
from apps.products.models import Deliver


class DeliverBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deliver
        fields = '__all__'
        extra_kwargs = {field_name: {'required': False} for field_name in model._meta.fields}


class DeliverCreateSerializer(DeliverBaseSerializer):
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    postal_code = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)


class DeliverUpdateSerializer(DeliverBaseSerializer):
    pass


class DeliverDeleteSerializer(DeliverBaseSerializer):
    pass


class DeliverSerializer(DeliverBaseSerializer):
    pass


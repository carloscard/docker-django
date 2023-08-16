from rest_framework import generics
from apps.products.models import Product
from apps.products.api.serializers.product_serializers import ProductSerializer, ProductCreateSerializer, \
    ProductUpdateSerializer
from apps.products.crud_products.crud_products import products


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return products.get_multi()


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return products.get(id=product_id)



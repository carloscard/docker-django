from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products.api.serializers import ProductSerializer, ProductCreateSerializer, ProductUpdateSerializer
from apps.products.models import Product


@api_view(['GET'])
def get_all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)


@api_view(['GET'])
def get_product_by_id(request, product_id):
    if request.method == 'GET':
        product = Product.objects.filter(id=product_id).first()
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)


@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        product_serializer = ProductCreateSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors)


@api_view(['PUT'])
def update_product(request, product_id):
    if request.method == 'PUT':
        product = Product.objects.filter(id=product_id).first()
        product_serializer = ProductUpdateSerializer(product, data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)

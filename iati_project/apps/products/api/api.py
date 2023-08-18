from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.products.api.serializers.product_serializers import ProductSerializer, ProductCreateSerializer, ProductUpdateSerializer
from apps.products.cruds.crud_products import products


@api_view(['GET'])
def get_all_products(request):
    if request.method == 'GET':
        # queryset
        products_query = products.get_multi()

        # validation
        if products_query:
            products_serializer = ProductSerializer(products_query, many=True)
            return Response(products_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'There are not products'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product_by_id(request, product_id):
    if request.method == 'GET':

        # queryset
        product_query = products.get(id=product_id)

        # valdiation
        if product_query:
            product_serializer = ProductSerializer(product_query)
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        product_serializer = ProductCreateSerializer(data=request.data)
        if product_serializer.is_valid():
            product_create = products.create(product_serializer)
            return Response(product_create.data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_product(request, product_id):
    if request.method == 'PUT':
        # queryset
        product_query = products.get(id=product_id)

        # validation
        if product_query:
            product_serializer = ProductUpdateSerializer(product_query, data=request.data)
            if product_serializer.is_valid():
                product_update = products.update(product_serializer)
                return Response(product_update.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

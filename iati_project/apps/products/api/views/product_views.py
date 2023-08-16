from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from apps.products.api.serializers.product_serializers import ProductSerializer, ProductCreateSerializer, \
    ProductUpdateSerializer, ProductDeleteSerializer
from apps.products.crud_products.crud_products import products


# View to list all Products
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return products.get_multi()


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    #lookup_url_kwarg = 'pk'

    def get_queryset(self, pk=None):
        #product_id = self.kwargs['pk']
        return products.get(id=pk).first()

    def get(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)


# View to create a single product
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            product_create = products.create(serializer)
            return Response(product_create.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        #product_id = self.kwargs['pk']
        return products.get(id=pk).first()

    def patch(self, request, pk=None):
        #product_query = self.get_queryset().filter(id=pk).first()
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            #product_serializer = self.serializer_class(product_query)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                #product_serializer.save()
                product_update = products.update(product_serializer)
                return Response(product_update.data, status= status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Logical deletion
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductDeleteSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return products.get(id=product_id)

    # Overwrite delete function to make a logical deletion
    def delete(self, request, pk=None):
        product_query = self.get_queryset().filter(id=pk).first()

        if product_query:
            product_query.state = False
            product_query.deleted_at = timezone.now()
            product_query.save()
            return Response(
                {'message': f'Product with id {product_query.id} has been deleted'}, status=status.HTTP_200_OK
            )

        return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

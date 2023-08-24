from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from apps.products.api.serializers.product_serializer import ProductSerializer, ProductCreateSerializer, \
    ProductUpdateSerializer, ProductDeleteSerializer
from apps.products.cruds.crud_products import products
from apps.products.cruds.crud_stock import stock_crud
import logging
from apps.products.models import Stock

logger = logging.getLogger(__name__)


class ProductViewSets(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    ## We will leave the READ methods to display them automatically,
    ## and we will override the rest (Update, create and delete)

    def get_queryset(self, pk=None):
        if pk is None:
            return products.get_multi()
        return products.get(id=pk).first()

    def create(self, request):
        """
        To create a product
        """
        self.serializer_class = ProductCreateSerializer
        logger.info(f'request data to create a product: {request.data}')
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            products.create(serializer)
            logger.info(f'product create response code: {status.HTTP_201_CREATED}')
            return Response({'message': 'Product created'}, status=status.HTTP_201_CREATED)

        logger.error(f'Error in product create: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        To update a product
        """
        self.serializer_class = ProductUpdateSerializer
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_update = products.update(product_serializer)
                logger.info(f'product update response code: {status.HTTP_200_OK}')
                return Response(product_update.data, status=status.HTTP_200_OK)

            logger.error(f'Error in product update: {product_serializer.errors}')
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        logger.error(f'Error in product update: Product not found')
        return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        To delete a product, logical deletion
        """
        self.serializer_class = ProductDeleteSerializer
        product_query = self.get_queryset(pk)
        if product_query:
            product_query.state = False
            product_query.deleted_at = timezone.now()
            product_query.save()
            logger.info(f'product destroy response code: {status.HTTP_200_OK}')
            return Response(
                {'message': f'Product with id {product_query.id} has been deleted'}, status=status.HTTP_200_OK
            )

        logger.error(f'Error in product destroy: Product not found')
        return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)


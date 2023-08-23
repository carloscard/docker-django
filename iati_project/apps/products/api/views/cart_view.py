from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.products.api.serializers.cart_serializer import CartSerializer, CartCreateSerializer, CartUpdateSerializer
from apps.products.cruds.crud_cart import cart_crud
from apps.products.api.controllers.controller_cart import ControllerProduct
import logging

logger = logging.getLogger(__name__)


class CartViewSets(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return cart_crud.get_multi()
        return cart_crud.get(id=pk).first()

    def create(self, request):
        """
        To create a cart
        """
        self.serializer_class = CartCreateSerializer
        logger.info(f'request data to create a cart: {request.data}')
        cart_create_serializer = self.serializer_class(data=request.data)

        if cart_create_serializer.is_valid():
            controller_product_obj = ControllerProduct(
                get_queryset=self.get_queryset,
                request=request,
                cart_create_serializer=cart_create_serializer
            )

            response, response_status = controller_product_obj.add_item_to_cart()
            logger.info(f'Product create response code {response_status}')
            return Response(response, status=response_status)

        return Response(cart_create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



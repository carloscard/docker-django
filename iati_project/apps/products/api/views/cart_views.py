from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.products.api.serializers.cart_serializers import CartSerializer, CartCreateSerializer, CartUpdateSerializer
from apps.products.cruds.crud_cart import cart_crud
from apps.products.cruds.crud_products import products
from apps.products.cruds.crud_stock import stock_crud


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
        cart_serializer = self.serializer_class(data=request.data)
        if cart_serializer.is_valid():

            product_id = request.data.get('product_id')
            product_quantity = request.data.get('product_quantity') or 1

            product_exist = products.get(id=product_id).first()

            if product_exist:
                stock = stock_crud.get_stock_by_product_id(product_id=product_id)
                current_stock = stock.current_stock
                if product_quantity <= current_stock:

                    if len(self.get_queryset()) > 0:

                        current_cart = self.get_queryset()[0]
                        request.data['product_quantity'] = current_cart.product_quantity + product_quantity
                        self.serializer_class = CartUpdateSerializer

                        cart_serializer = self.serializer_class(self.get_queryset(pk=current_cart.id), data=request.data)
                        if cart_serializer.is_valid():
                            cart_create = cart_crud.update(cart_serializer)

                    else:
                        cart_create = cart_crud.create(cart_serializer)
                    product_exist.cart_id = int(cart_create.data.get('id'))
                    current_stock = current_stock - product_quantity
                    stock.current_stock = current_stock
                    stock.save()
                    product_exist.save()

                    return Response(cart_serializer.data, status=status.HTTP_200_OK)

                else:
                    return Response({'message': 'Out of Stock'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)




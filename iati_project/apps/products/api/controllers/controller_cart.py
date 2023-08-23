from rest_framework import status
from apps.products.cruds.crud_products import products
from apps.products.cruds.crud_stock import stock_crud
from apps.products.cruds.crud_cart import cart_crud
from apps.products.api.serializers.cart_serializer import CartUpdateSerializer


class ControllerProduct:
    def __init__(self, get_queryset, request, cart_create_serializer):
        self.get_queryset = get_queryset
        self.request = request
        self.cart_create_serializer = cart_create_serializer

    def add_item_to_cart(self):
        product_id = self.request.data.get('product_id')

        # Si no hay valor en la petición, por defecto 1 producto
        product_quantity = self.request.data.get('product_quantity') or 1

        product_exist = products.get(id=product_id).first()

        if product_exist:
            stock = stock_crud.get_stock_by_product_id(product_id=product_id)

            current_stock = stock.current_stock

            # Comprobamos que la cantidad de producto no supere al stock actual
            if product_quantity <= current_stock:

                # Comprobamos si existe un carrito asociado al día de hoy
                if len(self.get_queryset()) > 0:

                    current_cart = self.get_queryset()
                    item_in_cart = False

                    # Se comprueba si el producto ya está en el carrito
                    for item in current_cart:
                        if item.product_id == product_id:
                            current_cart = item
                            item_in_cart = True

                    if item_in_cart:
                        # Update item
                        response, response_status = self.update_item(
                            current_cart=current_cart,
                            product_quantity=product_quantity
                        )

                    # Si no lo es, se añade un producto nuevo al carrito
                    else:
                        response, response_status = self.new_item(
                            added_item=product_exist
                        )

                # Si no existe lo creamos
                else:
                    response, response_status = self.new_item(
                        added_item=product_exist
                    )

                print("****++++**")
                print(response)
                print(response_status)
                if response_status in [200, 201]:
                    self.update_stock(
                        current_stock=current_stock,
                        product_quantity=product_quantity,
                        stock=stock
                    )
                return response, response_status

            else:
                response = {'message': 'Out of Stock'}
                response_status = status.HTTP_400_BAD_REQUEST
                return response, response_status

        response = {'message': 'Product not found'}
        response_status = status.HTTP_400_BAD_REQUEST
        return response, response_status

    def update_item(self, current_cart, product_quantity):

        self.request.data['product_quantity'] = current_cart.product_quantity + product_quantity
        print("^^^^^^")
        print(self.request.data['product_quantity'])
        if self.request.data['product_quantity'] < 0:
            response = {'message': f'You only have {current_cart.product_quantity} of this product in your basket'}
            response_status = status.HTTP_400_BAD_REQUEST
            return response, response_status

        update_serializer = CartUpdateSerializer

        if self.request.data['product_quantity'] == 0: self.request.data['state'] = False

        cart_update_serializer = update_serializer(
            self.get_queryset(pk=current_cart.id),
            data=self.request.data
        )

        if cart_update_serializer.is_valid():

            if self.request.data['product_quantity'] == 0:
                response = {'message': f'Item removed from the basket'}
            elif product_quantity > 0:
                response = {'message': f'{product_quantity*-1} Item has been removed from the basket'}
            else:
                response = {'message': f'{product_quantity} Item removed from the basket'}

            cart_crud.update(cart_update_serializer)
            response_status = status.HTTP_200_OK

            return response, response_status

        else:

            response = cart_update_serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST

            return response, response_status

    def new_item(self, added_item):
        cart_create = cart_crud.create(self.cart_create_serializer)

        # Asociamos el producto al carrito correspondiente
        added_item.cart_id = int(cart_create.data.get('id'))
        added_item.save()

        response = self.cart_create_serializer.data
        response_status = status.HTTP_201_CREATED

        return response, response_status

    def update_stock(self, current_stock, product_quantity, stock):
        # Actualizamos el stock
        current_stock = current_stock - product_quantity
        stock.current_stock = current_stock
        stock.save()

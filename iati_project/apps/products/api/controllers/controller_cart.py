from rest_framework import status
from apps.products.cruds.crud_products import products
from apps.products.cruds.crud_stock import stock_crud
from apps.products.cruds.crud_cart import cart_crud
from apps.products.api.serializers.cart_serializer import CartUpdateSerializer
import logging

logger = logging.getLogger(__name__)


class ControllerProduct:
    def __init__(self, get_queryset, request, cart_create_serializer):
        self.get_queryset = get_queryset
        self.request = request
        self.cart_create_serializer = cart_create_serializer

    def add_item_to_cart(self):
        product_id = self.request.data.get('product_id')

        # If no value is provided in the request, default to 1 produc
        product_quantity = self.request.data.get('product_quantity') or 1

        product_exist = products.get(id=product_id).first()

        if product_exist:
            stock = stock_crud.get_stock_by_product_id(product_id=product_id)

            current_stock = stock.current_stock

            # We check that the quantity of the product does not exceed the current stock
            if product_quantity <= current_stock:
                logger.info(f'product quantity <= current stock')

                # We check if there's a cart associated with today's date
                if len(self.get_queryset()) > 0:
                    logger.info(f'There is a cart created for today')
                    current_cart = self.get_queryset()
                    item_in_cart = False

                    # We check if the product is already in the cart
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

                    # If it's not, a new product is added to the cart
                    else:
                        if product_quantity <= 0:
                            logger.error(f'Negative quantity when add a new item')
                            response = {'message': 'No negative quantities when adding a new product'}
                            response_status = status.HTTP_400_BAD_REQUEST
                        else:
                            response, response_status = self.new_item(
                                added_item=product_exist
                            )

                # If the cart doesn't exist, we create it
                else:
                    logger.info(f'New cart')
                    if product_quantity <= 0:
                        logger.error(f'Negative quantity when creating a cart')
                        response = {'message': 'No negative quantities when creating a new cart'}
                        response_status = status.HTTP_400_BAD_REQUEST

                    else:
                        response, response_status = self.new_item(
                            added_item=product_exist
                        )

                if response_status in [200, 201]:
                    logger.info(f'Updating current stock')
                    self.update_stock(
                        current_stock=current_stock,
                        product_quantity=product_quantity,
                        stock=stock
                    )
                return response, response_status

            else:
                response = {'message': 'Out of Stock'}
                response_status = status.HTTP_400_BAD_REQUEST
                logger.error(f'Error in cart controller: Out of Stock')
                return response, response_status

        response = {'message': 'Product not found'}
        response_status = status.HTTP_400_BAD_REQUEST
        logger.error(f'Error in cart controller: Product not found')
        return response, response_status

    def update_item(self, current_cart, product_quantity):

        self.request.data['product_quantity'] = current_cart.product_quantity + product_quantity
        if self.request.data['product_quantity'] < 0:
            response = {'message': f'You only have {current_cart.product_quantity} of this product in your cart'}
            response_status = status.HTTP_400_BAD_REQUEST
            logger.error(f'Error in cart controller: Not enough product in the cart')
            return response, response_status

        update_serializer = CartUpdateSerializer

        if self.request.data['product_quantity'] == 0: self.request.data['state'] = False

        cart_update_serializer = update_serializer(
            self.get_queryset(pk=current_cart.id),
            data=self.request.data
        )

        if cart_update_serializer.is_valid():

            if self.request.data['product_quantity'] == 0:
                response = {'message': f'Product removed from the cart'}
            elif product_quantity > 0:
                response = {'message': f'{product_quantity} product/s added to the cart'}
            else:
                response = {'message': f'{product_quantity*-1} Product/s has been removed from the cart'}

            cart_crud.update(cart_update_serializer)
            response_status = status.HTTP_200_OK

            return response, response_status

        else:

            response = cart_update_serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST
            logger.error(f'Error in cart controller: {response}')

            return response, response_status

    def new_item(self, added_item):
        cart_create = cart_crud.create(self.cart_create_serializer)

        # We associate the product with the corresponding cart
        added_item.cart_id = int(cart_create.data.get('id'))
        added_item.save()

        response = {'message': 'Product added to the cart'}
        response_status = status.HTTP_201_CREATED

        return response, response_status

    def update_stock(self, current_stock, product_quantity, stock):
        # update the stock
        current_stock = current_stock - product_quantity
        stock.current_stock = current_stock
        stock.save()

from rest_framework.test import APITestCase
from apps.products.models import Product, Cart, Stock
from rest_framework import status
from apps.products.cruds.crud_cart import cart_crud


class CartTestCase(APITestCase):
    url_product = '/products/cart/'

    def create_cart(self):
        products = Product.objects.all()
        for product in products:
            response = self.client_class().post(
                self.url_product,
                {
                    "product_id": product.id
                },
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        cart_products = cart_crud.get_multi()

        for product in cart_products:
            self.assertEqual(product.product_quantity, 1)

    # Add 2 more products

    def add_more_products(self):
        products = Product.objects.all()
        for product in products:
            response = self.client_class().post(
                self.url_product,
                {
                    "product_quantity": 2,
                    "product_id": product.id
                },
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        cart_products = cart_crud.get_multi()

        for product in cart_products:
            self.assertEqual(product.product_quantity, 3)

    # We attempt to remove more products than are present in the basket
    def attempt_to_remove_excess_items(self):
        products = Product.objects.all()
        for product in products:
            response = self.client_class().post(
                self.url_product,
                {
                    "product_quantity": -5,
                    "product_id": product.id
                },
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def check_current_stock(self):
        stocks = Stock.objects.all()
        for stock in stocks:
            self.assertEqual(stock.current_stock, 7)

    # Here we remove all products in the cart
    def remove_all_products_from_cart(self):
        products = Product.objects.all()
        for product in products:
            response = self.client_class().post(
                self.url_product,
                {
                    "product_quantity": -3,
                    "product_id": product.id
                },
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def check_current_stock_after_remove_cart_items(self):
        stocks = Stock.objects.all()
        for stock in stocks:
            self.assertEqual(stock.current_stock, 10)

    # At this point, the basket should be empty
    def check_basket(self):
        cart_products = cart_crud.get_multi()
        for products in cart_products:
            self.assertEqual(products, None)


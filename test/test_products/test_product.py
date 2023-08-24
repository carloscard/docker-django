
from rest_framework import status
from test.test_setup import TestSetup
from test.test_cart.test_cart import CartTestCase


class ProductTestCase(TestSetup):
    # It can be done using reverse
    url_product = '/products/product/'

    def test_product(self):
        self.create_products()
        self.create_products_bad_format()
        self.show_products()

        # Cart testing
        test_cart = CartTestCase()
        test_cart.create_cart()
        test_cart.add_more_products()
        test_cart.attempt_to_remove_excess_items()
        test_cart.check_current_stock()
        test_cart.remove_all_products_from_cart()
        test_cart.check_current_stock_after_remove_cart_items()
        test_cart.check_basket()

    def create_products(self):
        response = self.client_class().post(
            self.url_product,
            {
                "material_composition": [2, 4, 3],
                "main_color": 1,
                "secondary_colors": [2, 4],
                "product_name": "Camiseta fashion 1",
                "brand": "adidas",
                "product_type_id": "T0002",
                "size": "M",
                "sizing_type": "UNISEX",
                "has_sleeves": True,
                "photo_url": "https://www.camisetas.com/1",
                "materials": [4, 2],
                "price": 10
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client_class().post(
            self.url_product,
            {
                "product_name": "Gorra fashion 1",
                "brand": "Lacoste",
                "product_type_id": "G0001",
                "photo_url": "https://www.gorras.com/1",
                "price": 15,
                "logo_color": 2,
                "main_color": "3",
                "secondary_colors": [4, 5],
                "materials": []

            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def create_products_bad_format(self):
        # We verify that if an incorrect product format is entered, the error code will be 400
        response = self.client_class().post(
            self.url_product,
            {
                "material_composition": [2, 4, 3],
                "main_color": 1,
                "secondary_colors": [2, 4],
                "product_name": "Camiseta fashion 1",
                "brand": "adidas",
                "product_type_id": "AAA2222",
                "size": "M",
                "sizing_type": "UNISEX",
                "has_sleeves": True,
                "photo_url": "https://www.camisetas.com/1",
                "materials": [4, 2],
                "price": 10
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def show_products(self):
        response = self.client_class().get(
            self.url_product,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # We verify that 2 products have been created
        self.assertEqual(len(response.data), 2)

        # Check each created product
        for product in response.data:

            response = self.client_class().get(
                f'{self.url_product}{product["id"]}/',
                format='json'
            )

            self.assertEqual(response.status_code, status.HTTP_200_OK)




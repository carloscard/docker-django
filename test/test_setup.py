from rest_framework.test import APITestCase
from test.mock_data.mock_product import MockProduct


class TestSetup(APITestCase):
    def setUp(self):
        # Records are created in the tables material color & Product
        MockProduct().insert_all()

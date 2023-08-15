from apps.products.models import Product
from apps.crud_base.crud_base import CRUDBase


class CRUDProducts(CRUDBase):
    def __init__(self):
        super().__init__(Product)

    """ 
    def get_multi(self):
        products = self.model.objects.filter(brand="nike").all()
        return products
    """

products = CRUDProducts()

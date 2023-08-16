from apps.products.models import Product
from apps.base.crud_base import CRUDBase


class CRUDProducts(CRUDBase):
    def __init__(self):
        super().__init__(Product)

    """ 
    def get(self):
        products = self.model.objects.filter(brand="nike").all()
        return products
    """
    def get(self, id: int):
        return self.model.objects.filter(pk=id, state=True)

    def get_multi(self):
        return self.model.objects.filter(state=True).all()

products = CRUDProducts()

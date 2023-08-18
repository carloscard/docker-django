from apps.products.models import Stock
from apps.base.crud_base import CRUDBase


class CRUDStock(CRUDBase):
    def __init__(self):
        super().__init__(Stock)

    def get_stock_by_product_id(self, product_id: int):
        return self.model.objects.filter(product_id=product_id, state=True).first()





stock_crud = CRUDStock()
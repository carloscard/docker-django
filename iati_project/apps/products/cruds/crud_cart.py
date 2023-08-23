from django.utils import timezone
from apps.products.models import Cart
from apps.base.crud_base import CRUDBase


class CRUDCart(CRUDBase):
    def __init__(self):
        super().__init__(Cart)

    def get_multi(self):
        print("*****")
        print(timezone.now().date())
        return self.model.objects.filter(current_date=timezone.now().date(), state=True).all()


cart_crud = CRUDCart()
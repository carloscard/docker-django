from django.utils import timezone
from apps.products.models import Deliver
from apps.base.crud_base import CRUDBase


class CRUDDeliver(CRUDBase):
    def __init__(self):
        super().__init__(Deliver)


deliver_crud = CRUDDeliver()

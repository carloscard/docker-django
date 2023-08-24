from apps.products.models import CompositionMaterial
from apps.base.crud_base import CRUDBase


class CRUDColor(CRUDBase):
    def __init__(self):
        super().__init__(CompositionMaterial)

    def get_color_name_by_id(self, pk: int):
        return self.model.objects.filter(pk=pk, state=True).values('color_name').first().get('color_name', None)


color_crud = CRUDColor()
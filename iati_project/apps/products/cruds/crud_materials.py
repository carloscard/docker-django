from apps.products.models import Material
from apps.base.crud_base import CRUDBase


class CRUDMaterial(CRUDBase):
    def __init__(self):
        super().__init__(Material)

    def get_material_name_by_id(self, pk: int):
        return self.model.objects.filter(pk=pk, state=True).values('material_name').first().get('material_name', None)


material_crud = CRUDMaterial()
from apps.products.models import Product
from apps.base.crud_base import CRUDBase
from django.utils import timezone
from django.db.models import Case, When, Value, CharField
from enumchoicefield import ChoiceEnum
from apps.products.cruds.crud_colors import color_crud
from apps.products.cruds.crud_materials import material_crud


class ProductType(ChoiceEnum):
    CAP = 'G0001'
    TSHIRT = 'T0002'


class CRUDProducts(CRUDBase):
    def __init__(self):
        super().__init__(Product)

    def get(self, id: int):
        return self.model.objects.filter(pk=id, state=True)

    def get_multi(self):

        # Order by caps then t-shirts
        orden_case = Case(
            When(product_type_id=str(ProductType.CAP), then=Value(1)),
            When(product_type_id=str(ProductType.TSHIRT), then=Value(2)),
            default=Value(3),  # If there are other values, they will be sorted at the end
            output_field=CharField(),
        )

        return self.model.objects.filter(state=True).order_by('product_type_id').order_by(orden_case,
                                                                                          '-created_at').all()

    def create(self, obj_in):
        is_cap = obj_in.validated_data.get('product_type_id').upper() == str(ProductType.CAP)
        is_t_shirt = obj_in.validated_data.get('product_type_id').upper() == str(ProductType.TSHIRT)

        main_color = f"main_color={color_crud.get_color_name_by_id(obj_in.validated_data.get('main_color'))}&"
        logo_color = f"logo_color={color_crud.get_color_name_by_id(obj_in.validated_data.get('logo_color'))}&"
        secondary_colors = "secondary_colors="

        for color in obj_in.validated_data.get('secondary_colors'):
            secondary_colors += f'{color_crud.get_color_name_by_id(color)}&'

        if is_cap:
            data_to_join = [
                f"product_name={obj_in.validated_data.get('product_name')}&",
                f"product_type={obj_in.validated_data.get('product_type_id')}&",
                f"brand={obj_in.validated_data.get('brand')}&",
                main_color,
                logo_color,
                secondary_colors,
                f"inclusion_year={timezone.now().year}"
            ]
            obj_in.validated_data['size'] = None
            obj_in.validated_data['has_sleeves'] = None
            description = ''.join(data_to_join)

        elif is_t_shirt:
            materials = "materials="
            for material in list(obj_in.validated_data.get('materials')):
                materials += f'{material_crud.get_material_name_by_id(material)}&'

            data_to_join = [
                f"product_name={obj_in.validated_data.get('product_name')}&",
                f"product_type={obj_in.validated_data.get('product_type_id')}&",
                f"brand={obj_in.validated_data.get('brand')}&",
                main_color,
                secondary_colors,
                materials,
                f"size={obj_in.validated_data.get('brand')}&",
                f"inclusion_year={timezone.now().year}"
            ]

            description = ''.join(data_to_join)

        obj_in.validated_data['description'] = description

        obj_in.save()
        return obj_in


products = CRUDProducts()

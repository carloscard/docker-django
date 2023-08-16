from django.db import models
from apps.base.models import BaseModel
from django.contrib.postgres.fields import ArrayField
from enumchoicefield import ChoiceEnum, EnumChoiceField


class SizingType(ChoiceEnum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    UNISEX = 'UNISEX'


# Create your models here.

class Product(BaseModel):
    product_name = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    product_type_id = models.CharField(max_length=50)
    main_color = models.IntegerField()
    secondary_colors = ArrayField(models.IntegerField(null=True), null=True)
    logo_color = models.IntegerField()
    size = models.CharField(max_length=10)
    materials = models.ManyToManyField('Material', related_name='product', through='CompositionMaterial', null=True)
    sizing_type = EnumChoiceField(enum_class=SizingType, default=SizingType.UNISEX)
    has_sleeves = models.BooleanField(null=True)
    photo_url = models.URLField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.CharField(max_length=250)
    deleted_at = models.DateTimeField('Deleted date', null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

        indexes = [
            models.Index(fields=['product_type_id'], name='product_type_id_index'),
            models.Index(fields=['secondary_colors'], name='secondary_colors_index')
        ]

    def __str__(self):
        return self.product_name


class Material(BaseModel):
    material_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __str__(self):
        return self.material_name


class CompositionMaterial(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    percentage = models.IntegerField()

    class Meta:
        verbose_name = 'CompositionMaterial'
        verbose_name_plural = 'CompositionMaterials'

    def __str__(self):
        return f'{self.product_id} enrolled in {self.material_id}'


class Color(BaseModel):
    color_name = models.CharField(max_length=20)
    hex = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.color_name


class Stock(BaseModel):
    inclusion_date = models.DateField('Inclusion date')
    initial_stock = models.IntegerField()
    current_stock = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'



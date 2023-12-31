# Generated by Django 4.2.4 on 2023-08-17 09:06

import apps.products.models
from django.db import migrations, models
import enumchoicefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_cart_product_product_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='inclusion_date',
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizing_type',
            field=enumchoicefield.fields.EnumChoiceField(default=apps.products.models.SizingType(3), enum_class=apps.products.models.SizingType, max_length=6, null=True),
        ),
    ]

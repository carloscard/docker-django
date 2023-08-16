# Generated by Django 4.2.4 on 2023-08-16 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_rename_material_id_compositionmaterial_material_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.cart'),
        ),
    ]

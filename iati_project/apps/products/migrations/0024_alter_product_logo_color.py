# Generated by Django 4.2.4 on 2023-08-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_cart_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo_color',
            field=models.IntegerField(null=True),
        ),
    ]
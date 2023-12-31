# Generated by Django 4.2.4 on 2023-08-15 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_created_at_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='has_sleeves',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]

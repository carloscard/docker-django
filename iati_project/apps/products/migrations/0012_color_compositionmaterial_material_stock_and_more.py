# Generated by Django 4.2.4 on 2023-08-16 13:06

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update date')),
                ('color_name', models.CharField(max_length=20)),
                ('hex', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='CompositionMaterial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update date')),
                ('percentage', models.IntegerField()),
            ],
            options={
                'verbose_name': 'CompositionMaterial',
                'verbose_name_plural': 'CompositionMaterials',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update date')),
                ('material_name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update date')),
                ('inclusion_date', models.DateField(verbose_name='Inclusion date')),
                ('initial_stock', models.IntegerField()),
                ('current_stock', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='Deleted date'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='description', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='secondary_colors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='product',
            name='sizing_type',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('UNISEX', 'UNISEX')], default='UNISEX', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='logo_color',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_color',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=10),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['product_type_id'], name='product_type_id_index'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['secondary_colors'], name='secondary_colors_index'),
        ),
        migrations.AddField(
            model_name='stock',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='compositionmaterial',
            name='material_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.material'),
        ),
        migrations.AddField(
            model_name='compositionmaterial',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='materials',
            field=models.ManyToManyField(related_name='product', through='products.CompositionMaterial', to='products.material'),
        ),
    ]

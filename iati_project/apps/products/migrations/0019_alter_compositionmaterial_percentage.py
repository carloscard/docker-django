# Generated by Django 4.2.4 on 2023-08-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_compositionmaterial_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compositionmaterial',
            name='percentage',
            field=models.IntegerField(default=100, null=True),
        ),
    ]

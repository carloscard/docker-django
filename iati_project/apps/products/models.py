from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    product_type_id = models.CharField(max_length=50)
    main_color = models.CharField(max_length=50)  # This could be a ForeignKey to a Colors table
    #secondary_colors = models.ManyToManyField('Color', related_name='secondary_products')
    logo_color = models.CharField(max_length=50) # This could be a ForeignKey to a Colors table
    size = models.CharField(max_length=20) # This could be a ForeignKey to a Sizes table
    #composition_id = models.IntegerField()  # This could be a ForeignKey to a Materials table
    #sizing = models.CharField(max_length=50)  # Enum equivalent
    has_sleeves = models.BooleanField(null=True)
    photo_url = models.URLField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

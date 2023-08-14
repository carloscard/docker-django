from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    product_type_id = models.IntegerField()
    main_color = models.IntegerField()  # This could be a ForeignKey to a Colors table
    #secondary_colors = models.ManyToManyField('Color', related_name='secondary_products')
    logo_color = models.IntegerField()  # This could be a ForeignKey to a Colors table
    size = models.IntegerField()  # This could be a ForeignKey to a Sizes table
    #composition_id = models.IntegerField()  # This could be a ForeignKey to a Materials table
    #sizing = models.CharField(max_length=50)  # Enum equivalent
    has_sleeves = models.BooleanField()
    photo_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

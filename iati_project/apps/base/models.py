from django.db import models


# Abstract class
class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    created_at = models.DateTimeField('Creation date', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Update date', null=True)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'

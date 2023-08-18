
from typing import Type, TypeVar
from django.db import models
ModelType = TypeVar("ModelType", bound=models.Model)


class CRUDBase:
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        Delete will be an Update. It's a good practice to make a logic delete

        **Parameters**
        * `model`
        """
        self.model = model

    def get_multi(self)-> ModelType:
        return self.model.objects.all()

    def get(self, id: int) -> ModelType:
        return self.model.objects.filter(pk=id)

    def create(self, obj_in) -> ModelType:
        obj_in.save()
        return obj_in

    def update(self, obj_in) -> ModelType:
        obj_in.save()
        return obj_in


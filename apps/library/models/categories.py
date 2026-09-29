from django.db import models

from apps.base.models import OrderedModel


class CategoryModel(OrderedModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

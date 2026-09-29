from django.db import models

from apps.base.models import OrderedModel


class GenreModel(OrderedModel):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='sub_genres'
    )

    def __str__(self):
        return f'{self.parent} -> {self.name}' if self.parent else self.name

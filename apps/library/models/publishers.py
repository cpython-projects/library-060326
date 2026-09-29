from django.db import models

from apps.base.models import UUIDModel, TimeStampModel, SoftDeleteModel


class Publisher(UUIDModel, TimeStampModel, SoftDeleteModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
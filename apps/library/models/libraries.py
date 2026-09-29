from django.db import models
from apps.base.models import TimeStampModel


class LibraryModel(TimeStampModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    site = models.URLField(blank=True)

    def __str__(self):
        return self.name

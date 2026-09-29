from django.db import models

from apps.base.models import TimeStampModel
from .libraries import LibraryModel
from .members import MemberModel


class PostModel(TimeStampModel):
    title = models.CharField(max_length=100)
    body = models.TextField()

    author = models.ForeignKey(
        MemberModel,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    is_moderate = models.BooleanField(default=False)
    library = models.ForeignKey(
        LibraryModel,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    def __str__(self):
        return self.title

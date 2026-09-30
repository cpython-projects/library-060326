from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.base.models import TimeStampModel
from .books import BookModel
from .libraries import LibraryModel


class BorrowModel(TimeStampModel):
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    book = models.ForeignKey(
        BookModel,
        on_delete=models.PROTECT,
    )
    library = models.ForeignKey(
        LibraryModel,
        on_delete=models.PROTECT,
    )
    borrow_date = models.DateField(
        default=timezone.localdate,
    )
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.member} -> {self.book} -> {self.due_date:%d/%m/%Y}'

    class Meta:
        default_related_name = 'borrows'

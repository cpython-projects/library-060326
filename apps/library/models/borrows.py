from django.db import models
from django.utils import timezone

from apps.base.models import TimeStampModel
from .books import BookModel
from .libraries import LibraryModel
from .members import MemberModel


class BorrowModel(TimeStampModel):
    member = models.ForeignKey(
        MemberModel,
        on_delete=models.PROTECT,
        related_name='borrows',
    )
    book = models.ForeignKey(
        BookModel,
        on_delete=models.PROTECT,
        related_name='borrows',
    )
    library = models.ForeignKey(
        LibraryModel,
        on_delete=models.PROTECT,
        related_name='borrows',
    )
    borrow_date = models.DateField(
        default=timezone.localdate,
    )
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.member} -> {self.book} -> {self.due_date:%d/%m/%Y}'

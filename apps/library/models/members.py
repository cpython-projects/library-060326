from django.db import models

from apps.base.models import TimeStampModel, UUIDModel, SoftDeleteModel
from .choices import Gender, MemberRole
from .libraries import LibraryModel
from .validators import member_age_validator


class MemberModel(UUIDModel, TimeStampModel, SoftDeleteModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    birth_date = models.DateField(
        validators=[member_age_validator, ]
    )

    libraries = models.ManyToManyField(
        LibraryModel,
        related_name='members',
        blank=True,
    )
    role = models.CharField(
        max_length=1,
        choices=MemberRole.choices,
        default=MemberRole.READER,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

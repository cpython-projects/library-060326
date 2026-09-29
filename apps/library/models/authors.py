from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.base.models import UUIDModel, TimeStampModel, SoftDeleteModel
from .choices import Gender
from .validators import author_birth_date_validator


class AuthorModel(UUIDModel, TimeStampModel, SoftDeleteModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(
        validators=[author_birth_date_validator],
    )
    death_date = models.DateField(null=True, blank=True)
    profile = models.URLField(blank=True)
    rating = models.FloatField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return (f'{self.last_name} {self.first_name[0]}.,'
                f' {self.birth_date} - {self.death_date if self.death_date else ""}')


class AuthorDetailModel(UUIDModel, TimeStampModel):
    author = models.OneToOneField(AuthorModel, on_delete=models.CASCADE, related_name='details')

    biography = models.TextField()
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
    )
    birth_city = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'Author\'s details: {self.gender}, {self.birth_city}, {self.biography[:20]}...'

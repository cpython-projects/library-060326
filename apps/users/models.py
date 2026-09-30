from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.base.models import UUIDModel
from apps.library.models.choices import Gender
from apps.library.models.validators import member_age_validator


class User(UUIDModel, AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    birth_date = models.DateField(
        validators=[member_age_validator, ], null=True, blank=True
    )

    REQUIRED_FIELDS = ['email']

    class Meta(AbstractUser.Meta):
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    def has_role(self, role):
        return self.groups.filter(name=role).exists()



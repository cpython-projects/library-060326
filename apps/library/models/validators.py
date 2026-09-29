from django.core.exceptions import ValidationError
from django.utils import timezone


def calculate_age(birth_date):
    today = timezone.localdate()
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )


def author_birth_date_validator(value):
    if calculate_age(value) < 18:
        raise ValidationError('Author must have at least 18 years old')


def member_age_validator(value):
    if not 6 <= calculate_age(value) <= 120:
        raise ValidationError('Member must be between 6 and 120 years old')

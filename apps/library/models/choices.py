from django.db import models


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'


class MemberRole(models.TextChoices):
    ADMIN = 'A', 'admin'
    READER = 'R', 'reader'
    STAFF = 'S', 'staff'

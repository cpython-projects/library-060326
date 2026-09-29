from django.core.validators import MinValueValidator
from django.db import models

from apps.base.models import TimeStampModel, UUIDModel
from .authors import AuthorModel
from .categories import CategoryModel
from .genres import GenreModel
from .publishers import Publisher


class BookModel(UUIDModel, TimeStampModel):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(
        AuthorModel,
        through='BookAuthorModel',
        related_name='books'
    )
    published_date = models.DateField()
    genres = models.ManyToManyField(GenreModel, related_name='books')
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )
    summary = models.TextField()
    page_count = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title


class BookAuthorModel(models.Model):
    class Role(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        COAUTHOR = 'COAUTHOR', 'Co-author'
        TRANSLATOR = 'TRANSLATOR', 'Translator'
        ILLUSTRATOR = 'ILLUSTRATOR', 'Illustrator'

    book = models.ForeignKey(
        BookModel,
        on_delete=models.CASCADE,
        related_name='book_authors'
    )
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.CASCADE,
        related_name='author_books'
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.AUTHOR,
    )

    def __str__(self):
        return f'{self.book} {self.author} {self.role}'

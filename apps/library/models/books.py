from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

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
        return f'{self.title}'

    class Meta:
        db_table = 'books'
        ordering = ['published_date'] # - - DESC 10...1
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        get_latest_by = 'published_date'
        # indexes = [
        #     models.Index(fields=['published_date', 'category'], name='books_published_date_idx'),
        #     models.Index(fields=['-published_date'], name='books_published_date_idx'),
        # ]
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['title', 'authors', 'category'],
        #         name='unique_category_title'
        #     ),
        #     models.CheckConstraint(
        #         condition=models.Q(page_count__gt=0),
        #         name='page_count_gt_0'
        #     )
        # ]


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


import os
from datetime import date

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.library.models import BookModel, CategoryModel, AuthorModel, MemberRole, BookAuthorModel

# books = BookModel.objects.all()
# for item in books:
#     print(item)

# category_it = CategoryModel.objects.get(slug='it')
#
# book_python = BookModel.objects.create(
#     title='Python',
#     published_date=date(2020, 1, 1),
#     summary='Python Book',
#     page_count=100,
#     category=category_it
# )
#
# fitzgerald = AuthorModel.objects.create(
#     first_name='F. Scott',
#     last_name='Fitzgerald',
#     birth_date=date(1896, 9, 24),
#     death_date=date(1940, 12, 21),
# )
#
# translator = AuthorModel.objects.create(
#     first_name='Scott',
#     last_name='Scott 1',
#     birth_date=date(1896, 9, 24),
#     death_date=date(1940, 12, 21),
# )
#
# book_python.authors.add(fitzgerald)
# book_python.authors.add(translator, through_defaults={'role': BookAuthorModel.Role.TRANSLATOR})


# book = BookModel.objects.get(pk='3141369d-7c57-4055-87e0-3a972f31acc0')
# book.title = 'Python Adv'
# book.save()


# books = BookModel.objects.all()
# books_100 = books.filter(page_count__gt=100)
# print(books_100)

#
# book_first = BookModel.objects.first()
# print(book_first)
# print('-' * 20)
# book_last = BookModel.objects.last()
# print(book_last)
# print('-' * 20)
# book_earliest = BookModel.objects.earliest()
# print(book_earliest)
# print('-' * 20)
# book_latest = BookModel.objects.latest()
# print(book_latest)


# author = AuthorModel.objects.filter(rating__gt=3, first_name='John')
# print(author)
#
# author = AuthorModel.objects.filter(rating__gt=3).filter(first_name='John')
# print(author)
#
#
# author = AuthorModel.objects.filter(rating__gt=3).filter(first_name='John')
# print(author)
#
# author = AuthorModel.objects.filter(rating__gt=3).filter(first_name='John').order_by('-first_name')
# print(author)
#
# print(AuthorModel.objects.count())
# print(BookModel.objects.exists())

# query = BookModel.objects.values('title', 'published_date', 'category')
# for row in query:
#     print(type(row))
#     print(f"Название: {row['title']}, дата: {row['published_date']}, {row['category']}")

# books = BookModel.objects.filter(page_count__gt=300, published_date__lt=date(1950, 1, 1))
# print(books)
#
# books = BookModel.objects.filter(title__exact='The Great Gatsby')   # с учетом регистра
# print(books)
# books = BookModel.objects.filter(title__iexact='the great gatsby')  # без
# print(books)
#
# books = BookModel.objects.filter(title__contains='python')
# print(books)
# books = BookModel.objects.filter(title__icontains='python')
# print(books)

# books = BookModel.objects.filter(title__startswith='py')
# print(books)
# books = BookModel.objects.filter(title__istartswith='py')
# print(books)
# books = BookModel.objects.filter(title__endswith='ON')
# print(books)
# books = BookModel.objects.filter(title__iendswith='ON')
# print(books)

#
# books = BookModel.objects.filter(pk__in=[1, 2, 3])
# print(books)
# books = BookModel.objects.filter(category__slug__in=['classic', 'it'])
# print(books)
#
# books = BookModel.objects.filter(published_date__gt=date(2000, 1, 1))
# print(books)

# books = BookModel.objects.filter(published_date__year=2025)
# print(books)
#
# books = BookModel.objects.filter(page_count__range=(100, 300))
# print(books)

# book = BookModel.objects.filter(category__isnull=False).count()
# print(book)

from django.db.models import Q

# books = BookModel.objects.filter(Q(page_count__range=(100, 300)) | Q(category__isnull=False))
# print(books)
# books = BookModel.objects.filter(Q(page_count__range=(100, 300)) & Q(category__isnull=False))
# books = BookModel.objects.filter(page_count__range=(100, 300), category__isnull=False)
# books = BookModel.objects.filter(page_count__range=(100, 300)).filter(category__isnull=False)
#
# books = BookModel.objects.filter(~Q(category__slug='classic'))
# import uuid
# ids = uuid.uuid4(), uuid.uuid4()
# print(ids)
# books = BookModel.objects.filter(~Q(pk__in=ids))
# print(books)
#
#
# books = BookModel.objects.filter(
#     ~Q(category__slug__in=['classic', 'it']) & Q(page_count__gt=300)
# )
#
# print(books)


query = Q()
title = 'Python'
page_count = None
if title:
    query &= Q(title__icontains=title)
if page_count:
    query &= Q(page__gte=page_count)

books = BookModel.objects.filter(query)
for book in books:





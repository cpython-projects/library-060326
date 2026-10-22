import os

import django
import logging
from django.db.models import F, Count
from django.db.models.functions import ExtractYear, ExtractQuarter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

sql_logger = logging.getLogger('django.db.backends')
sql_logger.setLevel(logging.DEBUG)
sql_logger.addHandler(logging.StreamHandler())


from apps.library.models import BookModel


# books = BookModel.objects.filter(published_date__year=2021)
# for book in books:
#     print(book, book.published_date)


# books = BookModel.objects.filter(published_date__month=2)
# for book in books:
#     print(book, book.published_date)


# books = BookModel.objects.filter(published_date__quarter=4)
# for book in books:
#     print(book.title, book.published_date)

# books = BookModel.objects.filter(published_date__week_day=1)
# for book in books:
#     print(book.title, book.published_date)
#
# print('#' * 20)

# books = BookModel.objects.filter(published_date__iso_week_day__in=[1, 2])
# for book in books:
#     print(book.title, book.published_date)


# books = BookModel.objects.annotate(year=ExtractYear('published_date')).order_by('-year')
# for book in books:
#     print(book.title, book.year, book.published_date)



# books = BookModel.objects.annotate(quarter=ExtractQuarter('published_date')).filter(quarter__in=(1, 2))
# for book in books:
#     print(book.title, book.quarter, book.published_date)

# books_per_year = (BookModel.objects
#                   .annotate(year=ExtractYear('published_date'))
#                   .values_list('year')
#                   .annotate(book_count=Count('id'))
#                   .order_by('-book_count')
#                   )
#
# print(type(books_per_year))
#
# for book in books_per_year:
#     # print(book['year'], book['book_count'])
#     print(book)









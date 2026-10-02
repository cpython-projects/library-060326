import os
from django.utils import timezone

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.library.models import BookModel, CategoryModel, AuthorModel, MemberRole, BookAuthorModel

# classic = CategoryModel.objects.get(slug='it')
# books = BookModel.objects.filter(title__contains='python')
# for item in books:
#     print(item.title, item.category)
#
# classic = CategoryModel.objects.get(slug='classic')
# BookModel.objects.filter(title__contains='python').update(
#     category=classic,
#     updated_at=timezone.now(),
# )
# books = BookModel.objects.filter(title__contains='python')
# for item in books:
#     print(item.title, item.category)


# books = BookModel.objects.filter(title__contains='python')
# for item in books:
#     print(item.title, item.category, item.page_count)


# books = BookModel.objects.filter(title__contains='python')
# for item in books:
#     item.page_count += 10
#     item.save(update_fields=['page_count'])
from django.db.models import F

# BookModel.objects.filter(title__contains='python').update(
#     page_count=F('page_count') + 10,
#     updated_at=timezone.now(),
# )
# books = BookModel.objects.filter(title__contains='python')
# for item in books:
#     print(item.title, item.category, item.page_count)



books = BookModel.objects.all()[:5]
print(type(books))

books = BookModel.objects.all()[2:5]
print(type(books))

books = BookModel.objects.all()[::2]
print(type(books))

books = BookModel.objects.all()[::-1]
print(type(books))

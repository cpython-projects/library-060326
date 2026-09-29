"""
Заполнение базы тестовыми данными.

    python manage.py seed_library          — добавить данные
    python manage.py seed_library --clear  — удалить старые данные и заполнить заново
"""
import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from faker import Faker

from apps.library.models import (
    AuthorDetailModel,
    AuthorModel,
    BookModel,
    BorrowModel,
    CategoryModel,
    GenreModel,
    LibraryModel,
    MemberModel,
    PostModel,
    Publisher,
)
from apps.library.models.choices import Gender, MemberRole

fake = Faker('ru_RU')


class Command(BaseCommand):
    help = 'Заполняет базу тестовыми данными'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Удалить старые данные перед заполнением')

    @transaction.atomic  # если что-то упадёт, в базу не запишется ничего
    def handle(self, *args, **options):
        if options['clear']:
            self.clear()

        # 1. Справочники
        publishers = [
            Publisher.objects.create(
                name=fake.company()[:100],
                address=fake.street_address(),
                city=fake.city(),
                country=fake.country(),
            )
            for _ in range(10)
        ]
        self.stdout.write(self.style.SUCCESS(f'Publishers: {len(publishers)} created'))

        categories = [
            CategoryModel.objects.create(name=name, slug=slug, position=i)
            for i, (name, slug) in enumerate([
                ('Классика', 'classic'),
                ('Для детей', 'kids'),
                ('Детектив', 'detective'),
                ('Психология', 'psychology'),
                ('IT', 'it'),
                ('Фантастика', 'fiction'),
            ])
        ]
        self.stdout.write(self.style.SUCCESS(f'Categories: {len(categories)} created'))

        detective = GenreModel.objects.create(name='Детектив', position=1)
        fantasy = GenreModel.objects.create(name='Фантастика', position=2)
        genres = [
            detective,
            fantasy,
            GenreModel.objects.create(name='Психологический детектив', parent=detective, position=1),
            GenreModel.objects.create(name='Киберпанк', parent=fantasy, position=1),
        ]
        self.stdout.write(self.style.SUCCESS(f'Genres: {len(genres)} created'))

        libraries = [
            LibraryModel.objects.create(
                name=f'Библиотека им. {fake.last_name()}',
                location=fake.street_address(),
                site=fake.url(),
            )
            for _ in range(3)
        ]
        self.stdout.write(self.style.SUCCESS(f'Libraries: {len(libraries)} created'))

        # 2. Авторы и детали (один к одному)
        authors = []
        for _ in range(50):
            author = AuthorModel.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(minimum_age=20, maximum_age=100),
                rating=random.randint(1, 5),
            )
            AuthorDetailModel.objects.create(
                author=author,
                biography=fake.text(),
                birth_city=fake.city(),
                gender=random.choice(Gender.values),
            )
            authors.append(author)
        self.stdout.write(self.style.SUCCESS(f'Authors: {len(authors)} created'))

        # 3. Книги: авторы через BookAuthorModel, жанры через обычный M2M
        books = []
        for _ in range(100):
            book = BookModel.objects.create(
                title=fake.sentence(nb_words=3),
                published_date=fake.date_between(start_date='-50y', end_date='today'),
                summary=fake.text(),
                page_count=random.randint(100, 1000),
                category=random.choice(categories),
                publisher=random.choice(publishers),
            )
            book.authors.add(random.choice(authors))  # роль AUTHOR подставится по умолчанию
            book.genres.add(random.choice(genres))
            books.append(book)
        self.stdout.write(self.style.SUCCESS(f'Books: {len(books)} created'))

        # 4. Участники
        members = []
        for _ in range(30):
            member = MemberModel.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                gender=random.choice(Gender.values),
                birth_date=fake.date_of_birth(minimum_age=7, maximum_age=80),
                role=random.choice(MemberRole.values),
            )
            member.libraries.add(random.choice(libraries))
            members.append(member)
        self.stdout.write(self.style.SUCCESS(f'Members: {len(members)} created'))

        # 5. Посты
        posts = [
            PostModel.objects.create(
                title=fake.sentence(nb_words=5)[:100],
                body=fake.text(),
                author=random.choice(members),
                library=random.choice(libraries),
                is_moderate=random.choice([True, False]),
            )
            for _ in range(20)
        ]
        self.stdout.write(self.style.SUCCESS(f'Posts: {len(posts)} created'))

        # 6. Выдачи: часть уже вернули, часть ещё на руках
        today = timezone.localdate()
        borrows = []
        for _ in range(50):
            borrow_date = today - timedelta(days=random.randint(0, 60))
            due_date = borrow_date + timedelta(days=14)
            returned_date = None
            if due_date < today and random.choice([True, False]):
                returned_date = due_date
            borrows.append(BorrowModel.objects.create(
                member=random.choice(members),
                book=random.choice(books),
                library=random.choice(libraries),
                borrow_date=borrow_date,
                due_date=due_date,
                returned_date=returned_date,
            ))
        self.stdout.write(self.style.SUCCESS(f'Borrows: {len(borrows)} created'))

    def clear(self):
        # Порядок важен: сначала таблицы, которые ссылаются на другие (PROTECT)
        BorrowModel.objects.all().delete()
        PostModel.objects.all().delete()
        BookModel.objects.all().delete()        # вместе с ним удалятся BookAuthorModel
        AuthorModel.objects.all().delete()      # вместе с ним удалятся AuthorDetailModel
        MemberModel.objects.all().delete()
        GenreModel.objects.filter(parent__isnull=False).delete()  # сначала поджанры
        GenreModel.objects.all().delete()
        CategoryModel.objects.all().delete()
        LibraryModel.objects.all().delete()
        Publisher.objects.all().delete()
        self.stdout.write(self.style.WARNING('Old data deleted'))

"""
Пакет моделей приложения library.
"""

from .authors import AuthorModel, AuthorDetailModel
from .categories import CategoryModel
from .genres import GenreModel
from .publishers import Publisher
from .libraries import LibraryModel
from .books import BookModel, BookAuthorModel
from .posts import PostModel
from .borrows import BorrowModel
from .choices import MemberRole

__all__ = [
    'AuthorModel',
    'AuthorDetailModel',
    'CategoryModel',
    'GenreModel',
    'Publisher',
    'LibraryModel',
    'BookModel',
    'BookAuthorModel',
    'PostModel',
    'BorrowModel',
    'MemberRole',
]
from .func_base import book_list_create, book_detail
from .bvc_api_view import BookListCreateAPIView, BookDetailAPIView
from .borrows_api_view_class import BorrowListCreateAPIView


# from .generic_views import BookListCreateAPIView
from .generic_views import (BookListCreateAPIView,
                            BookRetrieveUpdateDestroyAPIView,
                            CategoryRetrieveUpdateDestroyAPIView,
                            CategoryListCreateAPIView,
BookDetailView
                            )
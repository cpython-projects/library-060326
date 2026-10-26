from django.urls import path
from .views import book_list_create, book_detail
from .views import BookDetailAPIView, BookListCreateAPIView
from .views import BorrowListCreateAPIView


# urlpatterns = [
#     path('books/', book_list_create, name='books'),
#     path('books/<uuid:pk>/', book_detail, name='books_detail'),
# ]


urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book_list_create'),
    path('books/<uuid:pk>/', BookDetailAPIView.as_view(), name='book_detail'),

    path('borrows/', BorrowListCreateAPIView.as_view(), name='borrows_list_create'),
    # path('borrows/<int:pk>/', BookDetailAPIView.as_view(), name='borrow'),
]

# localhost/books/2026/?category=Python&year=2026
from django.urls import path
from .views import book_list_create, book_detail
from .views import BookDetailAPIView, BookListCreateAPIView


# urlpatterns = [
#     path('books/', book_list_create, name='books'),
#     path('books/<uuid:pk>/', book_detail, name='books_detail'),
# ]


urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book_list_create'),
    path('books/<uuid:pk>/', BookDetailAPIView.as_view(), name='book_detail'),
]
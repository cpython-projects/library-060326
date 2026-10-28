from django.urls import path, include
# from .views import book_list_create, book_detail
# from .views import BookDetailAPIView, BookListCreateAPIView
# from .views import BorrowListCreateAPIView
# from .views import (BookListCreateAPIView,
#                     BookRetrieveUpdateDestroyAPIView,
#                     CategoryRetrieveUpdateDestroyAPIView,
#                     CategoryListCreateAPIView,
# BookDetailView
#                     )


from rest_framework.routers import DefaultRouter, SimpleRouter
from apps.library.views.viewsets import BookViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# urlpatterns = [
#     path('books/', book_list_create, name='books'),
#     path('books/<uuid:pk>/', book_detail, name='books_detail'),
# ]


# urlpatterns = [
    # path('books/', BookListCreateAPIView.as_view(), name='book_list_create'),
    # path('books/<uuid:pk>/', BookDetailAPIView.as_view(), name='book_detail'),

    # path('borrows/', BorrowListCreateAPIView.as_view(), name='borrows_list_create'),
    # path('borrows/<int:pk>/', BookDetailAPIView.as_view(), name='borrow'),

    # path('books-generic/', BookListView.as_view(), name='book_list_generic'),
    # path('books-generics-mixins/', BookListCreateAPIView.as_view(), name='book_list_generics_mixins'),

    # path('books/', BookListCreateAPIView.as_view(), name='book_list_create'),
    # path('books/<uuid:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book_detail'),
    # path('categories/', CategoryListCreateAPIView.as_view(), name='categories'),
    # path('categories/<slug:category_slug>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail'),
    # path('books-detail/<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
# ]

# localhost/books/2026/?category=Python&year=2026
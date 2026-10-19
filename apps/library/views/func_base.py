# from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404
from django.db.models import ProtectedError

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from apps.library.models import BookModel
from apps.library.serializers import BookListCreateSerializer, BookDetailSerializer


@api_view(['GET', 'POST'])
def book_list_create(request):
    if request.method == 'GET':
        books = BookModel.objects.select_related().prefetch_related('authors')
        serializer = BookListCreateSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = BookListCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(BookModel, pk=pk)

    if request.method == 'GET':
        serializer = BookDetailSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method in ('PUT', 'PATCH'):
        serializer = BookDetailSerializer(book,
                                          data=request.data,
                                          partial=request.method == 'PATCH'
                                          )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        try:
            book.delete()
        except ProtectedError:
            return Response(
                {
                    "Detail": "This book cannot be deleted."
                },
                status=status.HTTP_409_CONFLICT
            )
        return Response(status=status.HTTP_204_NO_CONTENT)


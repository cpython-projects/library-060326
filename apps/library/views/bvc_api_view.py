# from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from django.db.models import ProtectedError

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


from apps.library.models import BookModel
from apps.library.serializers import BookListCreateSerializer, BookDetailSerializer


class BookListCreateAPIView(APIView):
    def get(self, request):
        books = BookModel.objects.select_related('category', 'publisher').prefetch_related('authors')

        category = request.query_params.get('category', None)
        year = request.query_params.get('year', None)
        author = request.query_params.get('author', None)


        if category:
            category = category.strip()
            books = books.filter(category__name__icontains=category)
        if year:
            try:
                year = int(year)
            except ValueError:
                raise ValidationError("Year must be an integer.")

            books = books.filter(published_date__year=year)

        if author:
            books = books.filter(authors__last_name__icontains=author).distinct()

        serializer = BookListCreateSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        # books = BookModel.objects.select_related().prefetch_related('authors')
        # serializer = BookListCreateSerializer(books, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookListCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        serializer = BookListCreateSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        serializer = BookDetailSerializer(book,
                                          data=request.data,
                                          )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        serializer = BookDetailSerializer(book,
                                          data=request.data,
                                          partial=True
                                          )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)

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
from rest_framework import viewsets

from apps.library.models import BookModel, CategoryModel
from apps.library.serializers import BookListCreateSerializer, CategorySerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookListCreateSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
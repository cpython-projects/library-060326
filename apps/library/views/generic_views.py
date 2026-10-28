from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.response import Response
from rest_framework import generics, mixins



from apps.library.models import BookModel, BookAuthorModel, CategoryModel
from apps.library.serializers import BookListCreateSerializer, CategorySerializer
from serializers import BookDetailSerializer


# class BookListView(GenericAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookListCreateSerializer
#
#     def get(self, request, *args, **kwargs):
#         books = self.get_queryset()
#         serializer = self.get_serializer(books, many=True)
#         return Response(serializer.data)


# class BookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookListCreateSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class BookListCreateAPIView(ListCreateAPIView):
    queryset = BookModel.objects.prefetch_related('authors')
    serializer_class = BookListCreateSerializer
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ('category', 'genres',)
    search_fields = ('title', 'authors__last_name', )
    ordering_fields = ('published_date', 'page_count')
    ordering = ('-published_date',)
    filterset_fields = {
        'category__slug': ['exact'],
        'published_date': ['year', 'year__gte', 'year__lte'],
        'page_count': ['gt', 'lt'],
    }


    def perform_create(self, serializer):
        if serializer.validated_data.get('category') is None:
            serializer.save(category=CategoryModel.objects.get(slug='python'))
        else:
            serializer.save()

class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.prefetch_related('authors')
    serializer_class = BookListCreateSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'category_slug'


class BookDetailView(RetrieveAPIView):
    queryset = BookModel.objects.prefetch_related('genres')
    serializer_class = BookDetailSerializer


    def get_serializer_context(self):
        context = super().get_serializer_context()
        include = self.request.query_params.get('include_genres', 'false')
        context['include_genres'] = include == 'true'
        return context
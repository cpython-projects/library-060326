from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.utils import timezone

from apps.library.models import BorrowModel, BookModel


User = get_user_model()

class BorrowSerializer(ModelSerializer):
    member = serializers.SlugRelatedField(slug_field='email', read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_authors = serializers.StringRelatedField(source='book.authors', many=True, read_only=True)
    library_name = serializers.CharField(source='library.name', read_only=True)
    status = serializers.SerializerMethodField()
    days_left = serializers.SerializerMethodField()


    class Meta:
        model = BorrowModel
        fields = ['member', 'book_title', 'book_authors', 'library_name', 'status', 'days_left']


    def get_status(self, obj):
        if obj.returned_date:
            return 'returned'
        if obj.due_date < timezone.datetime.now().date():
            return 'overdue'
        return 'holding'

    def get_days_left(self, obj):
        if obj.returned_date:
            return None

        return (obj.due_date - timezone.datetime.now().date()).days


class BorrowCreateSerializer(ModelSerializer):
    member = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=BookModel.objects.all())
    days = serializers.IntegerField(write_only=True, min_value=1, max_value=30)

    class Meta:
        model = BorrowModel
        # fields = BorrowModel._meta.get_fields() + ['days']

    # def validate(self, data):
    #     pass
    #
    # def create(self, data):
    #     pass


class BorrowUpdateSerializer(ModelSerializer):
    pass




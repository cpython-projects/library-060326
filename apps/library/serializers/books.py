from rest_framework import serializers
from apps.library.models import BookModel, AuthorModel, CategoryModel



class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'


class BookListCreateSerializer(serializers.ModelSerializer):
    # authors = AuthorDetailSerializer(many=True)
    # category = serializers.StringRelatedField(read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', queryset=CategoryModel.objects.all())
    # category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())

    pages = serializers.IntegerField(
        source='page_count',
        min_value=1,
        error_messages={
            'min_value': 'No less than 1 page',
        }
    )


    class Meta:
        model = BookModel
        fields = ['title', 'category', 'pages']

    def create(self, validated_data):
        title_data = validated_data.pop('title').strip().upper()
        validated_data['title'] = title_data
        return BookModel.objects.create(**validated_data)

    def validate_title(self, value):
        if value.lower() in ('без названия', 'тест', 'test'):
            raise serializers.ValidationError("Title cannot be like 'без названия', 'тест', 'test'")
        return value




class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'


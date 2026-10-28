from rest_framework.serializers import ModelSerializer
from apps.library.models import CategoryModel


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'slug']

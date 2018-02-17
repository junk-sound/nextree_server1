from category.models import Category
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)
from topic.serializers import TopicCategorySerializer

'''CREATE SERIALIZER'''

class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category_name',
        ]

'''LIST SERIALIZER'''

class CategoryListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
        view_name='category:detail',
        lookup_field='slug'
    )
    class Meta:
        model = Category
        fields = [
            'category_name',
            'detail_url',
        ]

'''DETAIL SERIALIZER'''

class CategoryDetailSerializer(ModelSerializer):
    topic_list = SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'category_name',
            'slug',
            'topic_list',
        ]
    def get_topic_list(self, obj):
        return TopicCategorySerializer(obj.topic_set.all().order_by('-modify_date'), many=True).data

'''UPDATE SERIALIZER'''

class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category_name',
        ]


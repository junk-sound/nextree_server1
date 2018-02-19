from post.models import Post
from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        CharField,
                                        )

class SearchSerializer(ModelSerializer):
    search_text = CharField(max_length=200)
    class Meta:
        model = Post
        fields = [
            'search_text'
        ]
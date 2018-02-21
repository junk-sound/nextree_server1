from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from bookmark.models import Bookmark
from post.models import Post

class BookmarkCreateSerializer(ModelSerializer):

    class Meta:
        model = Bookmark
        fields = [
            'title',
        ]
    def create(self, validated_data):

        post_obj = Post.objects.get(title=validated_data['title'])
        user = validated_data['user']
        tema = post_obj.tema
        topic = tema.topic
        slug = post_obj.slug
        title = post_obj.title
        url = post_obj.url
        writer = post_obj.user
        description = post_obj.description
        post_modify_date = post_obj.modify_date
        post_published_date = post_obj.published_date

        bookmark_obj = Bookmark(
            user = user,
            writer = writer,
            topic= topic,
            tema = tema,
            slug = slug,
            title = title,
            url = url,
            description = description,
            post_modify_date=post_modify_date,
            post_published_date=post_published_date,
        )
        bookmark_obj.save()
        return validated_data

class BookmarkListSerializer(ModelSerializer):
    writer = SerializerMethodField()
    class Meta:
        model = Bookmark
        fields = [
            'title',
            'writer',
            'slug',
            'description',
            'post_modify_date',
            'post_published_date',
        ]
    def get_writer(self, obj):
        return obj.writer.fullname


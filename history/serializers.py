from rest_framework.serializers import (
    ModelSerializer,
)
from history.models import History
from post.models import Post


class HistoryCreateSerializer(ModelSerializer):

    class Meta:
        model = History
        fields = [
            'title',
        ]

    def create(self, validated_data):
        post_obj = Post.objects.get(title=validated_data['title'])
        user = validated_data['user']
        writer = post_obj.user
        tema = post_obj.tema
        slug = post_obj.slug
        title = post_obj.title
        url = post_obj.url
        description = post_obj.description
        post_modify_date = post_obj.modify_date
        post_published_date = post_obj.published_date

        history_obj = History(
            user = user,
            writer = writer,
            tema = tema,
            slug = slug,
            title = title,
            url = url,
            description = description,
            post_modify_date=post_modify_date,
            post_published_date=post_published_date,
        )
        history_obj.save()
        return validated_data


class HistoryListSerializer(ModelSerializer):
    class Meta:
        model = History
        fields = [
            'title',
            'writer',
            'slug',
            'description',
            'post_modify_date',
            'post_published_date',
        ]


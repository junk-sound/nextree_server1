from post.models import Post
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
    CharField,
)

class PostListSerializer(ModelSerializer):
    user = SerializerMethodField()
    tema = SerializerMethodField()
    detail_url = HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    class Meta:
        model = Post
        fields = [
            'tema',
            'title',
            'user',
            'description',
            'url',
            'create_date',
            'modify_date',
            'detail_url',
        ]
    def get_user(self, obj):
        return obj.user.fullname

    def get_tema(self, obj):
        return str(obj.tema)

class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    tema = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'tema',
            'title',
            'user',
            'description',
            'url',
            'create_date',
            'modify_date',
        ]
    def get_user(self, obj):
        return obj.user.fullname

    def get_tema(self, obj):
        return str(obj.tema.tema_name)

class PostTemaSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'title',
            'user',
            'description',
            'url',
            'create_date',
            'modify_date',
            'published_date',
        ]
    def get_user(self, obj):
        return 'N'+str(obj.user.th)+' '+obj.user.fullname

class PostCreateUpdateSerializer(ModelSerializer):
    tema = CharField()
    class Meta:
        model = Post
        fields = [
            'title',
            'tema',
            'url',
            'description',
            'published_date',
        ]


class MyWriteSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'title',
            'user',
            'description',
            'url',
            'create_date',
            'modify_date',
            'published_date',
        ]
    def get_user(self, obj):
        return obj.user.fullname


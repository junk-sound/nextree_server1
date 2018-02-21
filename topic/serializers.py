from topic.models import Topic
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
    CharField,
)
from tema.serializers import TemaDetailSerializer, TemaTopicSerializer



'''CREATE SERIALIZER'''


class TopicCreateUpdateSerializer(ModelSerializer):
    category = CharField()
    class Meta:
        model = Topic
        fields = [
            'topic_name',
            'category',
            'description'
        ]


'''LIST SERIALIZER'''


class TopicListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
        view_name='topic:detail',
        lookup_field='slug'
    )
    tema_list = SerializerMethodField()
    tema_count = SerializerMethodField()
    post_count = SerializerMethodField()
    user = SerializerMethodField()
    class Meta:
        model = Topic
        fields = [
            'topic_name',
            'detail_url',
            'user',
            'modify_date',
            'description',
            'tema_list',
            'tema_count',
            'post_count',
        ]
    def get_user(self, obj):
        return obj.user.fullname
    def get_tema_list(self, obj):
        return TemaTopicSerializer(obj.tema_set.all().order_by('order_num'),many=True).data
    def get_tema_count(self,obj):
        return obj.tema_set.count()
    def get_post_count(self,obj):
        post_count = 0
        for tema in obj.tema_set.all():
            post_count+=tema.post_set.count()
        return post_count

'''DETAIL SERIALIZER'''


class TopicDetailSerializer(ModelSerializer):
    tema_list = SerializerMethodField()
    tema_count =SerializerMethodField()
    post_count = SerializerMethodField()
    user = SerializerMethodField()
    class Meta:
        model = Topic
        fields = [
            'topic_name',
            'user',
            'modify_date',
            'description',
            'tema_list',
            'tema_count',
            'post_count',
        ]
    def get_user(self, obj):
        return obj.user.fullname
    def get_tema_list(self, obj):
        return TemaTopicSerializer(obj.tema_set.all().order_by('order_num'),many=True).data
    def get_tema_count(self,obj):
        return obj.tema_set.count()
    def get_post_count(self,obj):
        post_count = 0
        for tema in obj.tema_set.all():
            post_count+=tema.post_set.count()
        return post_count



'''TOPICCATEGORY SERIALIZER'''

class TopicCategorySerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = [
            'topic_name',
        ]

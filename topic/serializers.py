from topic.models import Topic
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)
from tema.serializers import TemaDetailSerializer, TemaTopicSerializer

'''CREATE SERIALIZER'''


class TopicCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = [
            'topic_name',
        ]


'''LIST SERIALIZER'''


class TopicListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
        view_name='topic:detail',
        lookup_field='slug'
    )
    class Meta:
        model = Topic
        fields = [
            'topic_name',
            'detail_url',
        ]



'''DETAIL SERIALIZER'''


class TopicDetailSerializer(ModelSerializer):
    tema_list = SerializerMethodField()
    class Meta:
        model = Topic
        fields = [
            'topic_name',
            'slug',
            'tema_list',
        ]
    def get_tema_list(self, obj):
        return TemaTopicSerializer(obj.tema_set.all().order_by('order_num'),many=True).data

from tema.models import Tema
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)
from django.db.models import F

from post.serializers import PostTemaSerializer


'''STANDARD SERIALIZER'''


class StandardTemaSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = [
            'tema_name',
        ]


'''CREATE SERIALIZER'''


class TemaCreateSerializer(ModelSerializer):
    standard_tema = StandardTemaSerializer()

    class Meta:
        model = Tema
        fields = [
            'tema_name',
            'standard_tema',
        ]

    def create(self, validated_data):
        print('validated data:', validated_data)

        '''
        기준이 되는 객츼의 정보들을 파싱합니다.
        '''
        standard_tema_name = validated_data['standard_tema']['tema_name']
        standard_obj = Tema.objects.get(tema_name=standard_tema_name)
        standard_ordernum = standard_obj.order_num

        '''
        기존 객체들의 order_num을 update해줍니다.
        '''
        Tema.objects.filter(order_num__gt=standard_ordernum).update(order_num=F('order_num') + 1)

        '''
        새로운 객체를 저장합니다.
        '''
        tema_name = validated_data['tema_name']
        user = validated_data['user']
        topic = standard_obj.topic
        ordernum = standard_ordernum + 1
        Tema_obj = Tema(
            user=user,
            tema_name=tema_name,
            topic=topic,
            order_num=ordernum
        )
        Tema_obj.save()

        return validated_data


'''LIST SERIALIZER'''


class TemaListSerializer(ModelSerializer):
    topic = SerializerMethodField()
    detail_url = HyperlinkedIdentityField(
        view_name='tema:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Tema
        fields = [
            'topic',
            'tema_name',
            'order_num',
            'detail_url',
        ]

    def get_topic(self,obj):
        return(obj.topic.topic_name)



'''DETAIL SERIALIZER'''


class TemaDetailSerializer(ModelSerializer):
    topic = SerializerMethodField()
    user = SerializerMethodField()
    post_list = SerializerMethodField()
    class Meta:
        model = Tema
        fields = [
            'topic',
            'tema_name',
            'order_num',
            'user',
            'create_date',
            'modify_date',
            'post_list',
        ]
    def get_topic(self, obj):
        return (obj.topic.topic_name)


    def get_post_list(self, obj):
        return PostTemaSerializer(obj.post_set.all().order_by('-modify_date'), many=True).data

    def get_user(self, obj):
        # 여기서 obj는 tema object1, tema object2 다 나옴.
        return str(obj.user.username)


'''UPDATE SERIALIZER'''


class TemaUpdateSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = [
            'tema_name',
        ]


'''TEMATOPIC SERIALIZER'''


class TemaTopicSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = [
            'tema_name',
        ]

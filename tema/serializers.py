from tema.models import Tema
from topic.models import Topic
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
    CharField,
)
from django.db.models import F

from post.serializers import PostTemaSerializer
from rest_framework.exceptions import ParseError

'''STANDARD SERIALIZER'''
class StandardTemaSerializer(ModelSerializer):
    tema_name = CharField(allow_blank=True)
    class Meta:
        model = Tema
        fields = [
            'tema_name',
        ]


'''CREATE SERIALIZER'''


class TemaCreateSerializer(ModelSerializer):
    standard_tema = StandardTemaSerializer()
    topic = CharField(allow_blank=True)

    class Meta:
        model = Tema
        fields = [
            'tema_name',
            'topic',
            'standard_tema',
        ]

    def create(self, validated_data):
        '''
        기준이 되는 객츼의 정보들을 파싱합니다.
        '''
        if validated_data['topic']:
            topic_name = validated_data['topic']
            try:
                topic_obj = Topic.objects.get(topic_name=topic_name)
                standard_ordernum = 0
                ordernum = 1
            except:
                raise ParseError('There is no topic that you wrote')

        else:
            if validated_data['standard_tema']['tema_name']:
                standard_tema_name = validated_data['standard_tema']['tema_name']
                try:
                    standard_obj = Tema.objects.get(tema_name=standard_tema_name)
                    standard_ordernum = standard_obj.order_num
                    ordernum = standard_ordernum + 1
                    topic_obj = standard_obj.topic
                except:
                    raise ParseError('There is no standard tema that you wrrote')
            else:
                raise ParseError('You should type standard tema name')


        '''
        기존 객체들의 order_num을 update해줍니다.
        '''
        Tema.objects.filter(order_num__gt=standard_ordernum).update(order_num=F('order_num') + 1)

        '''
        새로운 객체를 저장합니다.
        '''
        tema_name = validated_data['tema_name']
        user = validated_data['user']

        Tema_obj = Tema(
            user=user,
            tema_name=tema_name,
            topic=topic_obj,
            order_num=ordernum
        )
        Tema_obj.save()

        return validated_data


'''LIST SERIALIZER'''


class TemaListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
        view_name='tema:detail',
        lookup_field='pk'
    )
    update = HyperlinkedIdentityField(
        view_name='tema:update',
        lookup_field='pk'
    )
    delete = HyperlinkedIdentityField(
        view_name='tema:delete',
        lookup_field='pk'
    )
    # latest_post_date = SerializerMethodField()
    class Meta:
        model = Tema
        fields = [
            'tema_name',
            'id',
            # 'order_num',
            'detail_url',
		    'modify_date',
            'update',
            'delete',
            # 'latest_post_date',
        ]

    # def get_latest_post_date(self, obj):
    #     print('get_latest_post_date')
    #     if len(obj.post_set.all()) != 0:
    #         latest_date = obj.post_set.all().order_by('-modify_date')[0].modify_date
    #     else:
    #         latest_date = None
    #     return latest_date




'''DETAIL SERIALIZER'''


class TemaDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    post_list = SerializerMethodField()
    post_count = SerializerMethodField()
    class Meta:
        model = Tema
        fields = [
            'tema_name',
            # 'order_num',
            'user',
            'create_date',
            'modify_date',
            'post_list',
            'post_count',
        ]

    def get_post_list(self, obj):
        return PostTemaSerializer(obj.post_set.all().order_by('-modify_date'), many=True).data

    def get_user(self, obj):
        # 여기서 obj는 tema object1, tema object2 다 나옴.
        return obj.user.fullname

    def get_post_count(self, obj):
        return obj.post_set.count()



'''UPDATE SERIALIZER'''


class TemaUpdateSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = [
            'tema_name',
        ]


'''TEMATOPIC SERIALIZER'''


class TemaTopicSerializer(ModelSerializer):
    post_count = SerializerMethodField()
    class Meta:
        model = Tema
        fields = [
            'tema_name',
            'id',
            'modify_date',
            'post_count'
        ]
    def get_post_count(self, obj):
        return obj.post_set.count()

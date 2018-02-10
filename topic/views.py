from django.shortcuts import render
from topic.models import Topic
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from topic.serializers import (
    TopicListSerializer,
    TopicCreateUpdateSerializer,
    TopicDetailSerializer
)

# Create your views here.


'''CREATE VIEW'''


class TopicCreateAPIView(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateUpdateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)


'''LIST VIEW'''


class TopicListAPIView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer


'''DETAIL VIEW'''


class TopicDetailAPIView(RetrieveAPIView):
    queryset = Topic.objects.all()
    # serializer_class = TopicDetailSerializer()
    lookup_field = 'slug'
    def get_serializer_class(self):
        print('check now2')
        print(self.request.query_params)
        TopicDetailSerializer(context={'request': self.request})
        return TopicDetailSerializer



'''UPDATE VIEW'''


class TopicUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateUpdateSerializer
    lookup_field = 'slug'


'''DELETE VIEW'''


class TopicDeleteAPIView(DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    lookup_field = 'slug'

from django.shortcuts import render
from topic.models import Topic
from category.models import Category
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)

from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from topic.serializers import (
    TopicListSerializer,
    TopicCreateUpdateSerializer,
    TopicDetailSerializer
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from topic.permissions import IsOwnerOrReadOnly

# Create your views here.


'''CREATE VIEW'''


class TopicCreateAPIView(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateUpdateSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        print('perform_create')
        category_name = self.request.data['category']
        try:
            category_obj = Category.objects.get(category_name=category_name)
        except:
            raise ParseError('Wrong category name: '+ category_name)

        print('out of tryexcept')

        # print(category_obj)

        # print(category_obj)
        serializer.save(user = self.request.user, category=category_obj)


'''LIST VIEW'''


class TopicListAPIView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer


'''DETAIL VIEW'''


class TopicDetailAPIView(RetrieveAPIView):
    queryset = Topic.objects.all()
    # serializer_class = TopicDetailSerializer()
    lookup_field = 'pk'
    def get_serializer_class(self):
        print('check now2')
        print(self.request.query_params)
        TopicDetailSerializer(context={'request': self.request})
        return TopicDetailSerializer



'''UPDATE VIEW'''


class TopicUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]


'''DELETE VIEW'''


class TopicDeleteAPIView(DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    lookup_field = 'pk'

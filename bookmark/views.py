from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView
from bookmark.models import Bookmark
from category.models import Category
from bookmark.serializers import (BookmarkCreateSerializer,
                                  BookmarkListSerializer,)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# Create your views here.


class BookmarkCreateAPIView(CreateAPIView):
    serializer_class = BookmarkCreateSerializer
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


# class BookmarkListAPIView(ListAPIView):
#     serializer_class = BookmarkListSerializer
#     def get_queryset(self):
#         queryset_list = Bookmark.objects.all().filter(user=self.request.user)
#         return queryset_list

class BookmarkDeleteAPIView(DestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkListSerializer
    lookup_field = 'slug'


class BookmarkListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        My_Bookmark_All_QS = Bookmark.objects.all().filter(user=request.user)
        Response_data = {}
        for category in Category.objects.all():
            category_name = category.category_name
            Response_data[category_name] = {}
            topic_QS = category.topic_set.all()
            for topic_Instance in topic_QS:
                topic_name = topic_Instance.topic_name
                My_Bookmark_Per_Topic_QS = My_Bookmark_All_QS.filter(topic=topic_Instance)
                serializer = BookmarkListSerializer(My_Bookmark_Per_Topic_QS, many=True)
                result_data = serializer.data
                Response_data[category_name][topic_name] = result_data

        return Response(Response_data, status=HTTP_200_OK)



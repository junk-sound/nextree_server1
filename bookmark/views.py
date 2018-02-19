from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from bookmark.models import Bookmark
from bookmark.serializers import (BookmarkCreateSerializer,
                                  BookmarkListSerializer,)
# Create your views here.


class BookmarkCreateAPIView(CreateAPIView):
    serializer_class = BookmarkCreateSerializer
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class BookmarkListAPIView(ListAPIView):
    serializer_class = BookmarkListSerializer
    def get_queryset(self):
        queryset_list = Bookmark.objects.all().filter(user=self.request.user)
        return queryset_list

class BookmarkDeleteAPIView(DestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkListSerializer
    lookup_field = 'slug'
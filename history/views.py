from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from history.models import History
from history.serializers import (HistoryCreateSerializer,
                                 HistoryListSerializer,)

# Create your views here.


class HistoryCreateAPIView(CreateAPIView):
    serializer_class = HistoryCreateSerializer
    queryset = History.objects.all()

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class HistoryListAPIView(ListAPIView):
    serializer_class = HistoryListSerializer

    def get_queryset(self):
        queryset_list = History.objects.all().filter(user=self.request.user)
        return queryset_list

class HistoryDeleteAPIView(DestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistoryListSerializer
    lookup_field = 'slug'
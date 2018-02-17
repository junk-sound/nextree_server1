from django.shortcuts import render
from tema.models import Tema
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from tema.serializers import (
    TemaListSerializer,
    TemaCreateSerializer,
    TemaUpdateSerializer,
    TemaDetailSerializer
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from tema.permissions import IsOwnerOrReadOnly

# Create your views here.

'''CREATE VIEW'''


class TemaCreateAPIView(CreateAPIView):
    # queryset = Tema.objects.all()
    serializer_class = TemaCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print('checking now1')
        print(self.request.data)
        serializer.save(user=self.request.user)


'''LIST VIEW'''


class TemaListAPIView(ListAPIView):
    queryset = Tema.objects.all().order_by('order_num')
    serializer_class = TemaListSerializer


'''DETAIL VIEW'''


class TemaDetailAPIView(RetrieveAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaDetailSerializer
    lookup_field = 'slug'


'''UPDATE VIEW'''


class TemaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


'''DELETE VIEW'''


class TemaDeleteAPIView(DestroyAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
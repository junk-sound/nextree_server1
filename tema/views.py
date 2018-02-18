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
from .permissions import IsOwnerOrReadOnly

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
    queryset = Tema.objects.all().order_by('-post__modify_date')
    serializer_class = TemaListSerializer

    # def get_queryset(self):
    #     print('get_queryset1')
    #     queryset_list = Tema.objects.all().order_by('modify_date')
    #     print('get_queryset2')
    #     for query in queryset_list:
    #         print(query)
    #         try:
    #             print(query.latest_post_date)
    #             print('good')
    #             print(query)
    #
    #
    #         except:
    #             print('bad')
    #             print(query)
    #
    #     return queryset_list


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
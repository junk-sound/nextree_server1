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
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print('checking now1')
        print(self.request.data)
        serializer.save(user=self.request.user)


'''LIST VIEW'''


class TemaListAPIView(ListAPIView):
    # queryset = Tema.objects.all().order_by('-post__modify_date')
    serializer_class = TemaListSerializer

    def get_queryset(self):
        queryset_unarranged = Tema.objects.all().order_by('-post__modify_date', '-modify_date')
        havepost_QS = Tema.objects.all().filter(post__isnull=False).order_by('-post__modify_date')
        nohavepost_QS = Tema.objects.all().filter(post__isnull=True).order_by('-modify_date')

        havepost_list = []
        nohavepost_list = []

        for query_hp in havepost_QS:
            if query_hp not in havepost_list:
                havepost_list.append(query_hp)

        for query_nhp in nohavepost_QS:
            if query_nhp not in nohavepost_list:
                nohavepost_list.append(query_nhp)

        havepost_list.extend(nohavepost_list)
        queryset_list = []
        for query in queryset_unarranged:
            if query not in queryset_list:
                queryset_list.append(query)
        return havepost_list


'''DETAIL VIEW'''


class TemaDetailAPIView(RetrieveAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaDetailSerializer
    lookup_field = 'pk'


'''UPDATE VIEW'''


class TemaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


'''DELETE VIEW'''


class TemaDeleteAPIView(DestroyAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaDetailSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly]

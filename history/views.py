from django.shortcuts import render
import datetime
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from rest_framework.views import (
    APIView,
)
from history.models import History
from post.models import Post
from history.serializers import (HistoryCreateSerializer,
                                 HistoryListSerializer,
                                 HistoryCreateUpdateSerializer,)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from account.permissions import IsOwnerOrReadOnly

# Create your views here.


class HistoryCreateUpdateAPIView(APIView):
    serializer_class = HistoryCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def post(self, request, *args, **kwargs):
        title = request.data['title']
        try:
            History_obj = History.objects.filter(user=request.user).get(title=title)
        except:
            History_obj = None
        if History_obj:

            History_obj.create_date = datetime.datetime.now()
            History_obj.save()

            return Response({'update':'successful'}, status=HTTP_200_OK)
        else:
            post_obj = Post.objects.get(title=title)
            user = request.user
            writer = post_obj.user
            tema = post_obj.tema
            slug = post_obj.slug
            title = post_obj.title
            url = post_obj.url
            description = post_obj.description
            post_modify_date = post_obj.modify_date
            post_published_date = post_obj.published_date

            History_obj = History(
                user=user,
                writer=writer,
                tema=tema,
                slug=slug,
                title=title,
                url=url,
                description=description,
                post_modify_date=post_modify_date,
                post_published_date=post_published_date,
            )
            History_obj.save()

            return Response({'create':'successful'}, status=HTTP_200_OK)


# class HistoryCreateAPIView(CreateAPIView):
#     serializer_class = HistoryCreateSerializer
#     queryset = History.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)


class HistoryListAPIView(ListAPIView):
    serializer_class = HistoryListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset_list = History.objects.all().filter(user=self.request.user)
        return queryset_list

class HistoryDeleteAPIView(DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = History.objects.all()
    serializer_class = HistoryListSerializer
    lookup_field = 'slug'
from django.shortcuts import render
from post.models import Post
from post.serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from post.permissions import IsOwnerOrReadOnly
from tema.models import Tema
from rest_framework.exceptions import ParseError
# Create your views here.


'''CREATE VIEW'''
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        tema_name = self.request.data['tema']
        try:
            tema_obj = Tema.objects.get(tema_name=tema_name)
        except:
            raise ParseError('wrong tema name: '+tema_name)



        serializer.save(user = self.request.user, tema=tema_obj)

'''LIST VIEW'''
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


'''DETAIL VIEW'''
class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all().order_by('-modify_date')
    serializer_class = PostDetailSerializer
    lookup_field = 'pk'

'''UPDATE VIEW'''
class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        tema_name = self.request.data['tema']
        try:
            tema_obj = Tema.objects.get(tema_name=tema_name)
        except:
            raise ParseError('wrong tema namev' + tema_name)
        serializer.save(user=self.request.user, tema=tema_obj)

'''DELETE VIEW'''
class PostDeleteAPIView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


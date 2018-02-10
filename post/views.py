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

# Create your views here.


'''CREATE VIEW'''
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(user = self.request.user)

'''LIST VIEW'''
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-modify_date')
    serializer_class = PostListSerializer

'''DETAIL VIEW'''
class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

'''UPDATE VIEW'''
class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)

'''DELETE VIEW'''
class PostDeleteAPIView(DestroyAPIView):
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


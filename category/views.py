from django.shortcuts import render
from category.models import Category
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

from category.serializers import (
    CategoryListSerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
    CategoryDetailSerializer,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from category.permissions import IsOwnerOrReadOnly

# Create your views here.

'''CREATE VIEW'''

class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

'''LIST VIEW'''

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all().order_by('-modify_date')
    serializer_class = CategoryListSerializer

'''DETAIL VIEW'''

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'

'''UPDATE VIEW'''
class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

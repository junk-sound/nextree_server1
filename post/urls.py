from django.urls import path
from post.views import (
    PostListAPIView,
    PostDetailAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
)
app_name = 'post'
urlpatterns = [
    # example url: /post/create/
    path('create/', PostCreateAPIView.as_view(), name = 'create'),
    # example url: /post/list/
    path('list/', PostListAPIView.as_view(), name = 'list'),
    # example url: /post/list/<slug_name>/
    path('list/<slug:slug>', PostDetailAPIView.as_view(), name = 'detail'),
    # example url: /post/list/<slug_name>/update/
    path('list/<slug:slug>/update/', PostUpdateAPIView.as_view(), name = 'update'),
    # example url: /post/list/<slug_name>/delete/
    path('list/<slug:slug>/delete/', PostDeleteAPIView.as_view(), name = 'delete'),

]
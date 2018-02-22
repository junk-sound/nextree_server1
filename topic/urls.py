from django.urls import path
from topic.views import (
    TopicListAPIView,
    TopicCreateAPIView,
    TopicUpdateAPIView,
    TopicDetailAPIView,
    TopicDeleteAPIView,
)
app_name = 'topic'
urlpatterns = [
    # example url: /topic/create/
    path('create/', TopicCreateAPIView.as_view(), name = 'create'),
    # example url: /topic/list/
    path('list/', TopicListAPIView.as_view(), name = 'list'),
    # example url: /topic/list/<slug_name>/
    path('list/<int:pk>/', TopicDetailAPIView.as_view(), name = 'detail'),
    # example url: /topic/list/<slug_name>/update/
    path('list/<int:pk>/update/', TopicUpdateAPIView.as_view(), name = 'update'),
    # example url: /topic/list/<slug_name>/delete/
    path('list/<int:pk>/delete/',TopicDeleteAPIView.as_view(), name = 'delete'),


    # # example url: /post/list/<slug_name>/<slug_post_name>/
    # path('list/<slug:slug>/<slug:slug>', TopicDetailPostAPIView.as_view(), name = 'detail_post'),
]
from django.urls import path
from tema.views import (
    TemaListAPIView,
    TemaCreateAPIView,
    TemaUpdateAPIView,
    TemaDetailAPIView,
    TemaDeleteAPIView,
)
app_name = 'tema'

urlpatterns = [
    # example url: /tema/create/
    path('create/', TemaCreateAPIView.as_view(), name = 'create'),
    # example url: /tema/list/
    path('list/', TemaListAPIView.as_view(), name = 'list'),
    # example url: /tema/list/<slug_name>/
    path('list/<slug:slug>', TemaDetailAPIView.as_view(), name = 'detail'),
    # example url: /tema/list/<slug_name>/update/
    path('list/<slug:slug>/update/', TemaUpdateAPIView.as_view(), name = 'update'),
    # example url: /tema/list/<slug_name>/delete/
    path('list/<slug:slug>/delete/',TemaDeleteAPIView.as_view(), name = 'delete'),


    # # example url: /post/list/<slug_name>/<slug_post_name>/
    # path('list/<slug:slug>/<slug:slug>', TemaDetailPostAPIView.as_view(), name = 'detail_post'),
]
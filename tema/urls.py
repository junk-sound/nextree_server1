from django.urls import path
from tema.views import (
    TemaListAPIView,
    TemaCreateAPIView,
    TemaUpdateAPIView,
    TemaDetailAPIView,
    TemaDeleteAPIView,
)
from django.utils.encoding import iri_to_uri
from django.utils.encoding import uri_to_iri
app_name = 'tema'



urlpatterns = [
    # example url: /tema/create/
    path('create/', TemaCreateAPIView.as_view(), name = 'create'),
    # example url: /tema/list/
    path('list/', TemaListAPIView.as_view(), name = 'list'),
    # example url: /tema/list/<slug_name>/
    path('list/<int:pk>/', TemaDetailAPIView.as_view(), name = 'detail'),
    # example url: /tema/list/<slug_name>/update/
    path('list/<int:pk>/update/', TemaUpdateAPIView.as_view(), name = 'update'),
    # example url: /tema/list/<slug_name>/delete/
    path('list/<int:pk>/delete/',TemaDeleteAPIView.as_view(), name = 'delete'),
    # # example url: /post/list/<slug_name>/<slug_post_name>/
    # path('list/<slug:slug>/<slug:slug>', TemaDetailPostAPIView.as_view(), name = 'detail_post'),
]
from django.urls import path
from category.views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDetailAPIView,
    CategoryDeleteAPIView,
)
app_name = 'category'

urlpatterns = [
    # example url: /category/create/
    path('create/', CategoryCreateAPIView.as_view(), name = 'create'),
    # example url: /category/list/
    path('list/', CategoryListAPIView.as_view(), name = 'list'),
    # example url: /category/list/<slug_name>/
    path('list/<slug:slug>/', CategoryDetailAPIView.as_view(), name = 'detail'),
    # example url: /category/list/<slug_name>/update/
    path('list/<slug:slug>/update/', CategoryUpdateAPIView.as_view(), name = 'update'),
    # example url: /category/list/<slug_name>/delete/
    path('list/<slug:slug>/delete/',CategoryDeleteAPIView.as_view(), name = 'delete'),


    # # example url: /post/list/<slug_name>/<slug_post_name>/
    # path('list/<slug:slug>/<slug:slug>', CategoryDetailPostAPIView.as_view(), name = 'detail_post'),
]
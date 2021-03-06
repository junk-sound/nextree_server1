from django.urls import path
from account.views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserListAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    MyWritePostAPIView,
)
from bookmark.views import (
    BookmarkCreateAPIView,
    BookmarkListAPIView,
    BookmarkDeleteAPIView,
)

from history.views import (
    # HistoryCreateAPIView,
    HistoryListAPIView,
    HistoryDeleteAPIView,
    HistoryCreateUpdateAPIView,
)

app_name = 'account'
urlpatterns = [
    # example url: /account/list/
    path('list/', UserListAPIView.as_view(), name = 'list'),
    # example url: /account/register/
    path('register/', UserCreateAPIView.as_view(), name = 'register'),
    # example url: /account/login/
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
    # example url: /account/update/
    path('update/<str:email>/', UserUpdateAPIView.as_view(), name = 'update'),
    # example url: /account/delete/<email>/
    path('delete/<str:email>/', UserDeleteAPIView.as_view(), name = 'delete'),
    # example url: /account/mywrite/
    path('mywrite/', MyWritePostAPIView.as_view(), name ='mywrite'),
    # example url: /account/bookmark/create/
    path('bookmark/create/', BookmarkCreateAPIView.as_view(), name = 'bookmark_create'),
    # example url: /account/bookmark/list/
    path('bookmark/list/', BookmarkListAPIView.as_view(), name = 'bookmark_list'),
    # example url: /account/bookmark/delete/<slug>/
    path('bookmark/delete/<int:pk>/', BookmarkDeleteAPIView.as_view(), name = 'bookmark_delete'),
    # # example url: /account/history/create/
    # path('history/create/', HistoryCreateAPIView.as_view(), name = 'history_create'),
    # example url: /account/histroy/createupdate/
    path('history/createupdate/',HistoryCreateUpdateAPIView.as_view(), name = 'history_createupdate'),
    # example url: /account/history/list/
    path('history/list/', HistoryListAPIView.as_view(), name = 'history_list'),
    # example url: /account/history/delete/<slug>/
    path('history/delete/<int:pk>/', HistoryDeleteAPIView.as_view(), name = 'history_delete'),
]
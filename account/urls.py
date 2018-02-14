from django.urls import path
from account.views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserListAPIView,
    UserUpdateAPIView,
)
app_name = 'account'
urlpatterns = [
    # example url: /account/list/
    path('list/', UserListAPIView.as_view(), name = 'list'),
    # example url: /account/register/
    path('register/', UserCreateAPIView.as_view(), name = 'register'),
    # example url: /account/update/
    path('update/<str:email>/', UserUpdateAPIView.as_view(), name = 'update'),
    # example url: /account/login/
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
]
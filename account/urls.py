from django.urls import path
from account.views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserListAPIView
)
app_name = 'account'
urlpatterns = [
    # example url: /account/list/
    path('list/', UserListAPIView.as_view(), name = 'list'),
    # example url: /account/register/
    path('register/', UserCreateAPIView.as_view(), name = 'register'),
    # example url: /account/login/
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
]
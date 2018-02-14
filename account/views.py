from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from rest_framework.views import APIView
# from django.contrib.auth.models import User
from account.models import User
from account.serializers import (UserDetailSerializer,
                                 UserCreateSerializer,
                                 UserLoginSerializer)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate

# Create your views here.

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print('request')
        print(request.data)
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            usr= authenticate(username=serializer.validated_data['username'],password=serializer.validated_data['password'])
            if usr is not None:
                print('usr')

                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(usr)
                token = jwt_encode_handler(payload)
                print('datadata')
                serializer.data['tok']=token
                print(serializer.data["username"])
                user_info = serializer.data
                print('new_data')
                print(user_info)
                response_data ={'msg': 'Login successful','id_pw':user_info, 'token': token}
                return Response(response_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.views import APIView
# from django.contrib.auth.models import User
from account.models import User
from account.serializers import (UserDetailSerializer,
                                 UserCreateSerializer,
                                 UserLoginSerializer,
                                 UserUpdateSerializer)

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

class UserUpdateAPIView(RetrieveUpdateAPIView):
    # queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = "email"
    def get_object(self):
        email = self.kwargs["email"]
        print('tttttt')
        return get_object_or_404(User, email=email)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    # def update(self, request, *args, **kwargs):
    #     serializer_data = request.data
    #     print('dddd')
    #     print(serializer_data)
    #     serializer = self.serializer_class(
    #         request.user, data=serializer_data, partial=True
    #     )
    #     serializer.is_valid(raise_exception=True)
    #
    #
    #     return Response(serializer.data, status=HTTP_200_OK)

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print('request111')
        print(request.data)
        print('request111')
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            usr= authenticate(email=serializer.validated_data['email'],password=serializer.validated_data['password'])
            if usr is not None:
                print('usr')
                print(usr.username)

                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(usr)
                token = jwt_encode_handler(payload)
                print('datadata')
                print(serializer.data["password"])
                input_info = serializer.data
                output_info = {"username":usr.username, "password":serializer.data["password"],"th":usr.th,"fullname":usr.fullname,"token":token}
                print('new_data')
                print(input_info)
                response_data ={'msg': 'Login successful','input_info':input_info, 'output_info':output_info}
                return Response(response_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


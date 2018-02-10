from rest_framework.serializers import (ModelSerializer,
                                        CharField,
                                        ValidationError,)
from django.contrib.auth.models import User
from django.db.models import Q

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'is_superuser',
            'is_staff',
            'is_active',
        ]

class UserCreateSerializer(ModelSerializer):
    # password2 = CharField(style={'input_type':'password'})
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
    extra_kwargs = {"password": {"write_only": True} }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(
            username=username,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

class UserLoginSerializer(ModelSerializer):
    token = CharField(read_only=True,allow_blank=True)
    username = CharField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]

    extra_kwargs = {"password":
                        {"write_only": True}
                    }
    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data['password']
        user = User.objects.filter(
            Q(username = username)
        ).distinct()
        print(user)
        # user = user.exclude(email__isnull=True).exclude(email__iexact=='')
        if user.exists() and user.count() ==1:
            user_obj = user.first()
        else:
            raise ValidationError('This username is not valid')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("incorect credential pls try again")

        data['token'] = "SOME RANDOM TOKEN"

        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data
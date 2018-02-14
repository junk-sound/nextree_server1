from rest_framework.serializers import (ModelSerializer,
                                        CharField,
                                        ValidationError,)
# from django.contrib.auth.models import User
from account.models import User
from django.db.models import Q


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
        ]

class UserCreateSerializer(ModelSerializer):
    confirm_password = CharField(style={'input_type':'password'})
    class Meta:
        model = User
        fields = [
            'email',
            'th',
            'username',
            'fullname',
            'password',
            'confirm_password',
        ]
    extra_kwargs = {"password": {"write_only": True}}
    def validate_email(self, value):
        print('aaaaaaaaaaaaaa')
        email_validate = value
        user_qs = User.objects.filter(email=email_validate)
        if user_qs.exists():
            raise ValidationError("This email has already registered.")
        return value

    def validate_username(self, value):
        username_validate = value
        user_qs = User.objects.filter(username=username_validate)
        if user_qs.exists():
            raise ValidationError("This username has already registered.")
        return value

    def validate_password(self,value):
        password1 = value
        data = self.get_initial()
        password2 = data.get("confirm_password")
        if password1 != password2:
            raise ValidationError("password must match")
        return value

    def validate_confirm_password(self,value):
        password2 = value
        data = self.get_initial()
        password1 = data.get("password")
        if password2 != password1:
            raise ValidationError("password must match")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        th = validated_data['th']
        fullname = validated_data['fullname']
        password = validated_data['password']

        user_obj = User(
            email=email,
            username=username,
            th=th,
            fullname=fullname
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserUpdateSerializer(ModelSerializer):
    email = CharField(required=False, allow_blank=True)
    ex_password =CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    new_password = CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    new_password_check = CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = User
        fields = [
            'email',
            'ex_password',
            'new_password',
            'new_password_check'
        ]

    def update(self, instance, validated_data):

        instance.set_password(validated_data.get('new_password'))
        instance.save()
        return instance

    def validate(self, data):
        print('vali')
        print(data)
        user_obj = None
        email=data.get("email",None)
        ex_password = data.get("ex_password",None)
        if not email:
            raise ValidationError("A email is required to update")
        if not ex_password:
            raise ValidationError("ex_password is required to update")
        user = User.objects.filter(
            Q(email=email)
        ).distinct()
        if user.exists() and user.count() ==1:
            user_obj = user.first()
        else:
            raise ValidationError('This email is not valid')
        if user_obj:
            if not user_obj.check_password(ex_password):
                raise ValidationError("incorrect ex_password please try again")
        return data

    def validate_new_password(self, value):
        data = self.get_initial()
        new_password = value
        new_password_check = data.get("new_password_check")
        if new_password != new_password_check:
            raise ValidationError("new password must match")
        return value
    def validate_new_password_check(self, value):
        data = self.get_initial()
        new_password_check = value
        new_password = data.get("new_password")
        if new_password_check != new_password:
            raise ValidationError("new password must match")
        return value


class UserLoginSerializer(ModelSerializer):
    email = CharField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]

    extra_kwargs = {"password":
                        {"write_only": True}
                    }
    def validate(self, data):
        print('data')
        print(data)
        user_obj = None
        email = data.get("email", None)
        password = data['password']
        if not email:
            raise ValidationError("A email is required to login")

        user = User.objects.filter(
            Q(email = email)
        ).distinct()
        # user = user.exclude(email__isnull=True).exclude(email__iexact=='')
        if user.exists() and user.count() ==1:
            user_obj = user.first()
        else:
            raise ValidationError('This email is not valid')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("incorrect password please try again")
        return data



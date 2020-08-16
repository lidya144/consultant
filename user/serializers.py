from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from models_app.models import User
from utilities.exception_handler import CustomValidation
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    """serializer for the users objects"""

    class Meta:
        model = User
        fields ="__all__"
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        user = User.objects.create_user(**validated_data)
        token, created = Token.objects.get_or_create(user=user)
      
        data = LoggedInUserSerializer(user)
        return {
            "user": data.data,
            "token": token.key,
        }

    def update(self, instance, validated_data):
        """Update a user """
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    """serializer for user login"""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    class Meta:
        model = User
        fields = ("email", "password")

    def validate(self, data):
        """Validate user data"""
        user = authenticate(
            email=data.get("email", None), password=data.get("password", None)
        )

        if not user:
            raise CustomValidation(
                "detail", "Invalid Credentials", status.HTTP_401_UNAUTHORIZED
            )
        

        token, created = Token.objects.get_or_create(user=user)
        data = LoggedInUserSerializer(user)
        return Response(
            {"user": data.data, "token": token.key,}, status=status.HTTP_200_OK,
        )


class LoggedInUserSerializer(serializers.ModelSerializer):
    """
    return the logged in user info
    """

    class Meta:
        model = User
        fields ="__all__"
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
        }

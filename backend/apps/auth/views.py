from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from apps.auth.serializers import EmailSerializer, PasswordSerializer, TokenPairSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

from .swagger.decorators import auth_activate_swagger, get_login_user_swagger, token_pair_swagger
from .swagger.serializers import SwaggerUserSerializer

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken
from drf_yasg.utils import swagger_auto_schema

UserModel: User = get_user_model()


@token_pair_swagger()
class TokenPairView(TokenObtainPairView):
    """
    Login
    """
    serializer_class = TokenPairSerializer


class AuthRegisterView(GenericAPIView):
    """
    Register user
    """

    serializer_class = UserSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: SwaggerUserSerializer()}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


@get_login_user_swagger()
class GetLoginUserView(RetrieveAPIView):
    """
    Info about login user
    """
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_object(self):
        return self.request.user


@auth_activate_swagger()
class ActivateUserView(GenericAPIView):
    """
    Activate account
    """
    @staticmethod
    def get(*args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckUserAndGetEmailForRecovery(GenericAPIView):
    """
    Get email for recovery password
    """
    serializer_class = EmailSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: ''}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_in_db = get_object_or_404(UserModel, email=serializer.data["email"])

        EmailService.recovery_password_email(user_in_db)

        return Response("check your email", status=status.HTTP_200_OK)


class RecoveryPassword(GenericAPIView):
    """
    Recover password with token
    """
    serializer_class = PasswordSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: ''}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        token = kwargs["token"]

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = JWTService.validate_token(token, RecoveryToken)

        user.set_password(serializer.data['password'])
        user.save()

        return Response(status=status.HTTP_200_OK)

from django.contrib.auth import get_user_model

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.response import Response

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer


class GetLoginUserView(GenericAPIView):
    def get(self, *args, **kwargs):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data, status.HTTP_200_OK)


class ActivateUserView(GenericAPIView):

    @staticmethod
    def get(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckUserAndGetEmailForRecovery(GenericAPIView):

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_in_db = get_object_or_404(UserModel, email=serializer.data["email"])

        EmailService.recovery_password_email(user_in_db)

        return Response("check your email", status=status.HTTP_200_OK)


class RecoveryPassword(GenericAPIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        token = kwargs["token"]

        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = JWTService.validate_token(token, RecoveryToken)

        user.set_password(serializer.data['password'])
        user.save()

        return Response(status=status.HTTP_200_OK)




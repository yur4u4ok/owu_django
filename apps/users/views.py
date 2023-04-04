from django.contrib.auth import get_user_model

from core.permissions.is_superuser import IsAdminUser, IsSuperUser

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.users.models import UserModel as User

from .serializers import UserSerializer

UserModel: User = get_user_model()


class AdminToUserView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_superuser or not user.is_staff:
            return Response('you cant do this with that user', status.HTTP_400_BAD_REQUEST)

        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserBlock(GenericAPIView):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_staff or not user.is_active:
            return Response('user cant be blocked', status.HTTP_400_BAD_REQUEST)

        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserUnblock(GenericAPIView):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_staff or user.is_active:
            return Response('user cant be unblocked', status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class GetAllUsersView(GenericAPIView):
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def get(self, *args, **kwargs):
        serializer = UserSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

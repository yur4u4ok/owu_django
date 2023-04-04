from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from apps.users.serializers import UserSerializer


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer


class GetLoginUserView(GenericAPIView):
    def get(self, *args, **kwargs):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)

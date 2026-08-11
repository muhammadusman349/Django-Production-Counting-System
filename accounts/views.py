from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User

from .serializers import LoginSerializer, RefreshTokenSerializer , UserSerializer


class LoginApiView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={"request": request}
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )


class RefreshTokenApiView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = RefreshTokenSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "access_token": serializer.validated_data["access_token"]
            },
            status=status.HTTP_200_OK
        )


class UserApiView(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            user = self.get_object()
            serializer = self.get_serializer(user)

            return Response(serializer.data)
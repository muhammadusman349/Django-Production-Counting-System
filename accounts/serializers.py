from rest_framework import serializers, status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "role",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"email": "Invalid email or password."},
                code=status.HTTP_401_UNAUTHORIZED
            )

        if not user.check_password(password):
            raise serializers.ValidationError(
                {"email": "Invalid email or password."},
                code=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:
            raise serializers.ValidationError(
                {"email": "This account is inactive."},
                code=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "email": user.email,
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
        }



class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)

    def validate(self, attrs):
        refresh_token = attrs.get("refresh_token")

        try:
            refresh = RefreshToken(refresh_token)

            attrs["access_token"] = str(refresh.access_token)

        except Exception:
            raise serializers.ValidationError(
                {"refresh_token": "Invalid or expired refresh token."}
            )

        return attrs
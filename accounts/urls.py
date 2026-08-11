from django.urls import path

from .views import (
    LoginApiView,
    RefreshTokenApiView,
    UserApiView,
)

urlpatterns = [
    path("login/", LoginApiView.as_view(), name="login"),
    path("refresh-token/", RefreshTokenApiView.as_view(), name="refresh-token"),
    # User List
    path("users/", UserApiView.as_view(), name="user-list"),
    # User Retrieve
    path("users/<int:id>/", UserApiView.as_view(), name="user-retrieve"),
]
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import (
    UserUpdateAPIView,
    PaymentListAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserCreateAPIView,
    UserDeleteAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete-update"),
    path("", UserListAPIView.as_view(), name="user-list"),
    path("user_detail/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
]

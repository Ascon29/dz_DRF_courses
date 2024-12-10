from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, PaymentListAPIView, UserListAPIView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("", UserListAPIView.as_view(), name="user-list"),
    path("user_detail/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
]

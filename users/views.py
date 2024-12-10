from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "course",
        "lesson",
        "payment_method",
    ]
    ordering_fields = [
        "payment_date",
    ]

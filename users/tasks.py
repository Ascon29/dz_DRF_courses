from datetime import timedelta

from celery.app import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_last_login():
    """Функция для проверки активности пользователей в сервисе.
    Блокирует их, при отсутствии активности более 30 дней."""
    users = User.objects.filter(is_active=True)
    date_now = timezone.now().date()

    for user in users:
        if not user.last_login:
            user.is_active = False
            user.save()
            print(f"пользователь {user} заблокирован")
        elif date_now - user.last_login.date() > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f"пользователь {user} заблокирован")

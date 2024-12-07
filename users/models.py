from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Введите почту (обязательно)")
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Имя", help_text="Введите имя")
    last_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Фамилия", help_text="Введите фамилию"
    )
    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="Телефон", help_text="Введите номер телефона"
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город", help_text="Введите город")
    avatar = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="Аватар", help_text="Загрузите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course, Lesson


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


class Payment(models.Model):
    CASH = "Наличные"
    NON_CASH = "Безналичный перевод"
    PAYMENT_CHOICES = ((CASH, "Наличные"), (NON_CASH, "Безналичный перевод"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    payment_date = models.DateField(verbose_name="Дата оплаты", help_text="Введите дату оплаты")
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный курс",
        help_text="Выберите оплаченный курс",
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный урок",
        help_text="Выберите оплаченный урок",
        blank=True,
        null=True,
    )
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты", help_text="Введите сумму оплаты")
    payment_method = models.CharField(
        choices=PAYMENT_CHOICES, max_length=50, verbose_name="Способ платежа", help_text="Выберите способ платежа"
    )

    class Meta:
        verbose_name = ("Оплата",)
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"{self.payment_date} {self.course} {self.amount}"

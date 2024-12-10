from django.db import models


class Course(models.Model):
    """Модель курса"""

    name = models.CharField(unique=True, max_length=100, verbose_name="Название курса", help_text="Введите название курса")
    description = models.TextField(
        verbose_name="Описание курса", help_text="Введите описание курса", blank=True, null=True
    )
    preview = models.ImageField(
        upload_to="courses/previews", verbose_name="Превью", help_text="Загрузите изображение", blank=True, null=True
    )

    def __str__(self):
        return f"Курс: {self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель урока"""

    name = models.CharField(
        unique=True, max_length=100, verbose_name="Название урока", help_text="Введите название урока"
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Введите описание урока", blank=True, null=True
    )
    preview = models.ImageField(
        upload_to="courses/previews", verbose_name="Превью", help_text="Загрузите изображение", blank=True, null=True
    )
    video = models.URLField(verbose_name="Видео", help_text="Ссылка на видео урок", blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", help_text="Выберите курс")

    def __str__(self):
        return f"Урок: {self.name} курс: {self.course}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

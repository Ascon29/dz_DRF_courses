from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """Тестирование CRUD урока."""

    def setUp(self):
        self.user = User.objects.create(email="for@test.ru")
        self.course = Course.objects.create(name="skypro", description="scypro_python")
        self.lesson = Lesson.objects.create(name="python", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тест на просмотр страницы одного урока."""

        url = reverse("courses:lesson-detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        """Тест на создание урока."""

        url = reverse("courses:lesson-create")
        data = {"name": "java", "course": 1}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """Тест на обновление урока."""

        url = reverse("courses:lesson-update", args=(self.lesson.pk,))
        data = {
            "name": "test update",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("name"), "test update")

    def test_lesson_delete(self):
        """Тест на удаление урока."""

        url = reverse("courses:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        """Тест на просмотр списка уроков."""

        url = reverse("courses:lesson-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "course": self.course.pk,
                    "description": None,
                    "preview": None,
                    "video": None,
                    "owner": self.user.pk,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    """Тестирование подписки."""

    def setUp(self):
        self.user = User.objects.create(email="for@test.ru")
        self.course = Course.objects.create(name="skypro", description="scypro_python")
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        """Тестирование на добавление подписки."""

        url = reverse("courses:subscription")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data, {"message": "подписка добавлена"})

    def test_subscription_delete(self):
        """Тестирование на удаление подписки."""

        url = reverse("courses:subscription")
        data = {"course": self.course.pk}
        Subscription.objects.create(course=self.course, user=self.user)  # Создаем подписку, чтобы было что удалить
        response = self.client.post(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data, {"message": "подписка удалена"})

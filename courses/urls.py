from django.urls import path

from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import (
    CourseViewSet,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonCreateAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    SubscriptionAPIView,
)

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-detail"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delete"),
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
] + router.urls

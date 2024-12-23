from rest_framework import serializers

from courses.models import Course, Lesson, Subscription
from courses.validators import YoutubeOnly


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для урока"""

    class Meta:
        model = Lesson
        fields = ["id", "name", "course", "description", "preview", "video", "owner"]
        validators = [YoutubeOnly(field="video")]


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для подписки"""

    class Meta:
        model = Subscription
        fields = ["user", "course"]


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курса"""

    lessons_count = serializers.SerializerMethodField()
    lessons_detail = LessonSerializer(source="lesson_set", many=True, read_only=True)
    subscription = SubscriptionSerializer(source="subscription_set", many=True, read_only=True)

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = ["id", "name", "description", "preview", "lessons_count", "lessons_detail", "owner", "subscription"]

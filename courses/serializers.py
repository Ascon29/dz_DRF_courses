from rest_framework import serializers

from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для урока"""

    class Meta:
        model = Lesson
        fields = ["id", "name", "course", "description", "preview", "video", "owner"]


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курса"""

    lessons_count = serializers.SerializerMethodField()
    lessons_detail = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = ["id", "name", "description", "preview", "lessons_count", "lessons_detail", "owner"]

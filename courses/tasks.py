from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from courses.models import Subscription


@shared_task
def notification(course_id, course_name):
    """Функция отправки уведомления пользователям, подписанным на курс, который был обновлен."""
    sub_courses = Subscription.objects.filter(course=course_id)
    email_list = [sub.user.email for sub in sub_courses]
    send_mail(
        subject="Обновление курса",
        message=f"Курс {course_name} был обновлен",
        from_email=EMAIL_HOST_USER,
        recipient_list=email_list,
    )

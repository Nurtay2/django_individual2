# notifications/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Notification
from students.models import Student
from grades.models import Grade

@shared_task
def send_daily_attendance_reminder():
    students = Student.objects.all()
    for student in students:
        send_mail(
            subject="Attendance Reminder",
            message="Please mark your attendance for today.",
            from_email="admin@school.com",
            recipient_list=[student.email],
        )
    return "Attendance reminder sent to all students."

@shared_task
def send_grade_update_notification(student_id, course_name, grade):
    student = Student.objects.get(id=student_id)
    message = f"A new grade for {course_name} has been posted: {grade}."
    send_mail(
        subject="Grade Update Notification",
        message=message,
        from_email="admin@school.com",
        recipient_list=[student.email],
    )
    return f"Grade update notification sent to {student.email}."

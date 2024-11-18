from django.db import models
from django.conf import settings

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=50)  # e.g., 'grade_update', 'attendance_reminder'

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.message[:20]}..."

from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

class StudentPermissionsTests(APITestCase):
    def setUp(self):
        self.student_user = get_user_model().objects.create_user(
            username="studentuser", password="studentpassword", role="Student"
        )
        self.teacher_user = get_user_model().objects.create_user(
            username="teacheruser", password="teacherpassword", role="Teacher"
        )
        self.client.login(username="studentuser", password="studentpassword")

    def test_student_access_own_profile(self):
        url = reverse("student-detail", args=[self.student_user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Create your tests here.

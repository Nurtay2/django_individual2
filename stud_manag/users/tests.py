from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

class UserRegistrationTests(APITestCase):
    def test_user_registration(self):
        url = reverse('user-register')
        data = {
            "username": "testuser",
            "password": "testpassword",
            "role": "Student"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)


# Create your tests here.

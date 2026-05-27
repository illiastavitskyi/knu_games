from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UserTests(TestCase):

    def test_register_page_opens(self):

        response = self.client.get('/users/register/')

        self.assertEqual(response.status_code, 200)


    def test_user_registration(self):

        response = self.client.post('/users/register/', {
            'username': 'testuser',
            'password': '12345'
        })

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            User.objects.filter(username='testuser').exists()
        )


    def test_login_works(self):

        User.objects.create_user(
            username='testuser',
            password='12345'
        )

        response = self.client.post('/users/login/', {
            'username': 'testuser',
            'password': '12345'
        })

        self.assertEqual(response.status_code, 302)
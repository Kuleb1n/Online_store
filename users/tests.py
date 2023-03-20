from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import User, EmailConfirmation


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('register')
        self.data = {
            'first_name': 'Name',
            'last_name': 'NAME',
            'username': 'NaMe21',
            'email': 'Name@mail.ru',
            'password1': 'Name1234',
            'password2': 'Name1234',
        }

    def test_register_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_post(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailConfirmation.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(email_verification.first().expiration.date(),
                         (now() + timedelta(hours=48)).date())

    def test_register_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(path=self.path, data=self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'A user with that username already exists.', html=True)

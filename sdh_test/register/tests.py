from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.auth.models import User

from .models import Profile

# Create your tests here.


class Register_Tests_Less_Five(TestCase):
    fixtures = ['initial_data.json']

    def test_register_page_exist(self):
        "testing main page exist"
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

    def test_raiting(self):
        """ Testing  request gets page """
        response = self.client.get(reverse('raiting'))
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        "testing login"
        args = {'username': 'andreev', 'password': 'Mirazh9379992'}
        response = self.client.post(reverse('login'),
                                    args)
        self.assertEquals(response.status_code, 302)

    def test_register(self):
        """ Testing  request saves changes """
        post = {
            'username': 'andreev2',
            'email': 'user@user.com',
            'password1': 'Mirazh9379992',
            'password2': 'Mirazh9379992',
            'invitation_code': 'MFN1875IJZPI'
        }
        response = self.client.post(
            reverse('register'),
            post)
        self.assertEquals(response.status_code, 302)
        self.client.post(
            reverse('register'),
            post,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(User.objects.all().count(), 3)
        user = User.objects.get(username='andreev2')
        inviter = Profile.objects.get(invitation_code='MFN1875IJZPI')
        self.assertEqual(user.email, post['email'])
        self.assertEqual(user.profile.inviter, inviter.user)
        self.assertEqual(len(mail.outbox), 1)

    def test_register_more_than_five(self):
        """ Testing  request saves changes """
        for i in range(4):
            post = {
                'username': 'andreev%s' % i,
                'email': 'user%s@user.com' % i,
                'password1': 'Mirazh9379992',
                'password2': 'Mirazh9379992',
                'invitation_code': ''
            }
            self.client.post(
                reverse('register'),
                post,
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertEqual(User.objects.all().count(), i + 3)
        self.assertEqual(User.objects.all().count(), 6)
        post = {
            'username': 'andreev6',
            'email': 'user@user.com',
            'password1': 'Mirazh9379992',
            'password2': 'Mirazh9379992',
            'invitation_code': ''
        }
        self.client.post(
            reverse('register'),
            post,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(User.objects.all().count(), 6)

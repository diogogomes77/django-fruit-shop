from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from users.models import ShopUser


class UserLoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        self.user = ShopUser.objects.create_user(**self.credentials)

    def test_login_success(self):
        response = self.client.post(
            reverse_lazy('login'),
            self.credentials,
            follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.context['user'].is_active)
        self.assertRedirects(response, reverse_lazy('home'))

    def test_login_fail(self):
        bad_credentials = {
            'username': 'testuser',
            'password': 'secret2'}
        response = self.client.post(
            reverse_lazy('login'),
            bad_credentials,
            follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)

    def test_logout(self):
        self.test_login_success()
        response = self.client.get(reverse_lazy('logout'))
        self.assertFalse(response.context['user'].is_active)

    def test_user_creation_after_login_fail(self):
        #  an logged user should not access user registration
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('signup'))
        self.assertEqual(403, response.status_code)


class UserCreationTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password1': 'secret',
            'password2': 'secret',
            'email': 'test@test.test'
        }

    def test_user_creation_sucess(self):
        response = self.client.post(
            reverse_lazy('signup'),
            self.credentials,
            follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_user_creation_email_sucess(self):
        # test the user registered with email
        response = self.client.post(
            reverse_lazy('signup'),
            self.credentials,
            follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertRedirects(response, reverse_lazy('login'))
        user = ShopUser.objects.get(username=self.credentials['username'])
        self.assertIsInstance(user, ShopUser)
        self.assertNotEqual(user.email, '')

    def test_user_creation_email_fail(self):
        # test the user registered without email
        self.credentials['email'] = ''
        response = self.client.post(
            reverse_lazy('signup'),
            self.credentials,
            follow=True
        )
        self.assertEquals(response.status_code, 200)
        users_qs = ShopUser.objects.filter(username=self.credentials['username'])
        self.assertEqual(len(users_qs), 0)


        

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profile.models import client
from django.contrib.auth import authenticate, login, logout
# Create your tests here.


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()  
        self.register_url = reverse('register')
        self.user = User.objects.create_user(username='testuser@gmail.com', password='12345')
    
    def test_userPage_POST_authenticated(self):
        self.client.login(username='testuser@gmail.com', password='12345')

        client_instance = client.objects.create(
            client=self.user,
            fullName='Test User',
            address1='123 Test St',
            address2='Apt 4B',
            state='TX',
            city='Testville',
            zipcode='12345'
        )           
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(client.objects.count(), 1)
        self.assertEqual(client.objects.first().fullName, 'Test User')

    def test_userPage_unauthenticated(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(client.objects.count(), 0)

    def test_userPage_GET(self):
        self.client.login(username='testuser', password='12345')

        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
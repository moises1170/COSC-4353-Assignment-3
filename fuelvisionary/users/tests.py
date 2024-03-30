
from django.test import TestCase, Client , RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse
from profile.models import client
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from users.views import loginPage, registerPage, homePage    

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_registerPage_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser2',
            'password': '12345'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)

    def test_registerPage_POST_no_data(self):
        response = self.client.post(self.register_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_homePage_GET(self):
        self.client.login(username='testuser', password='12345')

        response = self.client.get(self.home_url)
        
        self.assertEqual(response.status_code, 200)

    def test_homePage_GET_unauthenticated(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 302)


    def test_loginPage_POST_valid(self):
        user = User.objects.create_user(username='testuser2', password='12345')
        response = self.client.post(self.login_url, {
            'username': 'testuser2',
            'password': '12345'
        })

        self.assertEqual(response.status_code, 302)

    def test_loginPage_POST_invalid(self):
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_loginPage_GET(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)

    #Test for the userPage view


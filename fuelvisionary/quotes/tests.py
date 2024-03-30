from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from profile.models import client
from quotes.models import FuelQuote




class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.quote_url = reverse('fuelquote')
        self.history_url = reverse('quotehistory')
        self.home_url = reverse('home')
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.client_instance = client.objects.create(
            client=self.user,
            fullName='Test User',
            address1='123 Test St',
            address2='Apt 4B',
            state='TX',
            city='Testville',
            zipcode='12345'
        )

    def test_quote_POST(self):
        self.client.login(username='testuser', password='12345')
        current_client = client.objects.get(client=self.user)
        quote_instance = FuelQuote.objects.create(
            gallons=100,
            address= current_client.address1,
            date=  '2022-12-31',
            price= 10,
            total_price= 200,
            client= current_client
        )
        
        
        response = self.client.get(self.quote_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(FuelQuote.objects.count(), 1)
        self.assertEqual(FuelQuote.objects.first().gallons, 100)

    def test_history_GET(self):
        self.client.login(username='testuser', password='12345')

        FuelQuote.objects.create(
            gallons=100,
            address=self.client_instance.address1,  
            date='2022-12-31',
            price=2.5,
            total_price=250,
            client=self.client_instance
        )

        response = self.client.get(self.history_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '100')
from django.db import models
from profile.models import client

class FuelQuote(models.Model):
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    address = models.CharField(max_length=100)
    gallons = models.IntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    client = models.ForeignKey(client, on_delete=models.CASCADE)
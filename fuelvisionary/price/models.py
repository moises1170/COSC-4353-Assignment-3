from django.db import models
from profile.models import client
from quotes.models import FuelQuote

class Pricing(models.Model):
     location = models.CharField(max_length = 30, default="")
     rate_history = models.BooleanField(default=False)
     gallons = models.IntegerField(default=0)
     company_profit = models.FloatField(default=0.10)
     client = models.ForeignKey(client, on_delete=models.CASCADE)
     fuel_quote = models.OneToOneField(FuelQuote, on_delete=models.CASCADE)
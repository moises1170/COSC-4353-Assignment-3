from django.db import models
from profile.models import client
from quotes.models import FuelQuote


class Pricing(models.Model):
    location = models.CharField(max_length=30, default="")
    rate_history = models.BooleanField(default=False)
    gallons = models.IntegerField(default=0)
    company_profit = models.FloatField(default=0.10)
    fuel_quote = models.OneToOneField(FuelQuote, on_delete=models.CASCADE)

    def calculate_price(self):
        price_per_gallon = 1.50
        location_factor = 0.02 if self.location.upper() == "TX" else 0.04
        rate_history_factor = 0.01 if self.rate_history else 0
        gallons_requested_factor = 0.02 if self.gallons > 1000 else 0.03

        margin = price_per_gallon * (location_factor - rate_history_factor + gallons_requested_factor + self.company_profit)
        suggested_price = price_per_gallon + margin
        total_amount_due = suggested_price * self.gallons

        return suggested_price, total_amount_due

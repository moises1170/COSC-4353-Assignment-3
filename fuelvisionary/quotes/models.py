from django.db import models
# Create your models here.

class FuelQuote(models.Model):
    requested_gallons = models.PositiveIntegerField()
    delivery_date = models.DateField()
    delivery_address = models.CharField(max_length=255)
    price_per_gallon = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_due = models.DecimalField(max_digits=20, decimal_places=2)
    client = models.ForeignKey('profile.Client', on_delete=models.CASCADE)

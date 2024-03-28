from django.db import models
from django.core.validators import MinLengthValidator
from profile.models import client

# Create your models here.
# class for the fuel quotes
class fuel_quote(models.Model):
    gallonsRequested = models.PositiveIntegerField()
    deliveryAddress = models.CharField(max_length=100)
    deliveryDate = models.DateField()
    priceQuote = models.DecimalField(decimal_places=2, default=10, max_digits=10)
    amountDue = models.DecimalField(decimal_places=2, max_digits=10)
    client = models.ForeignKey(client, on_delete=models.CASCADE)

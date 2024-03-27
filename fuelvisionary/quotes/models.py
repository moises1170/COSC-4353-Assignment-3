from django.db import models
# Create your models here.

class FuelQuoteRequest(models.Model):
    requestedGallons = models.CharField(max_length = 10)
    deliveryDate = models.DateField(null = True)


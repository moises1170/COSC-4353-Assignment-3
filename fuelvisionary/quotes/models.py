from django.db import models
# Create your models here.

class FuelQuoteRequest(models.Model):
    requestedGallons = models.CharField(max_length = 10)
    deliveryDate = models.DateField(null = True)

    from django.db import models

class FuelQuote(models.Model):
    client = models.ForeignKey('profile.Client', on_delete=models.CASCADE, related_name='fuel_quotes')
    requested_gallons = models.IntegerField(validators=[MinValueValidator(1)])
    delivery_date = models.DateField()
    delivery_address = models.CharField(max_length=255, blank=True, null=True)
    price_per_gallon = models.DecimalField(max_digits=5, decimal_places=2)
    total_amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields as necessary

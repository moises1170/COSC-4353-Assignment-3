from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class client(models.Model):
    fullName = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=9, validators=[MinLengthValidator(5), ])
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    
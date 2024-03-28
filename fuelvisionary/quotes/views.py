from django.shortcuts import render
from profile.models import client
from .models import fuel_quote

# Create your views here.
def fuelQuote(request):
    if request.method == 'POST':
        gallonsRequested = request.POST.get("gallonsRequested")
        deliveryDate = request.POST.get("deliveryDate")
        priceQuote = 10
        totalDue = request.POST.get("totalDue")
        user_profile = client.objects.get(client=request.user)
        deliveryAddress = f"{user_profile.address1}, {user_profile.address2}, {user_profile.city}, {user_profile.state}, {user_profile.zipcode}"
        new_quote = fuel_quote.objects.create(gallonsRequested=gallonsRequested, deliveryAddress=deliveryAddress, deliveryDate=deliveryDate, priceQuote=priceQuote, totalDue=totalDue)
        
    return render(request, 'fuel_quote.html')
  
def quoteHistory(request):
    fuel_quotes = fuel_quote.objects.filter(client=request.user)
    return render(request, 'fuelQuoteHistory.html', {'fuel_quotes': fuel_quotes})
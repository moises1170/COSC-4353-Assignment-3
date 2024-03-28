from django.shortcuts import render

# Create your views here.
def fuelQuote(request):
    return render(request, 'fuel_quote.html')

def quoteHistory(request):
    return render(request, 'fuelQuoteHistory.html')
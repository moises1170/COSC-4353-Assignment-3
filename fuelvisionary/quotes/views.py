# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def quoteHistory(request):
    return render(request, 'fuel_quote.html')

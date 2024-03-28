from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import fuel_quote, client
from .forms import FuelQuoteForm  # Make sure to create this form


def fuelQuote(request):
    user_client = client.objects.get(client=request.user)
    if request.method == 'POST':
        form = FuelQuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.client = user_client
            # Assuming price and total due are calculated within the form's save method or elsewhere
            new_quote.save()
            return redirect('quoteHistory')  # Redirect to the history view or another appropriate page
    else:
        form = FuelQuoteForm()

    return render(request, 'fuel_quote.html', {'form': form})

def quoteHistory(request):
    user_client = client.objects.get(client=request.user)
    fuel_quotes = fuel_quote.objects.filter(client=user_client)
    return render(request, 'fuelQuoteHistory.html', {'fuel_quotes': fuel_quotes})

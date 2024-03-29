from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import FuelQuote
from .forms import FuelQuoteForm
from profile.models import client  
from django.contrib.auth.decorators import login_required

@login_required
def quote(request):
    
    current_client = client.objects.get(client=request.user)

   
    quote_count = FuelQuote.objects.filter(client=current_client).count()

    if request.method == 'POST':
        form = FuelQuoteForm(request.POST)
        if form.is_valid():
            FuelQuote.objects.create(
                gallons=form.cleaned_data['gallons'],
                address=current_client.address1,  
                date=form.cleaned_data['date'],
                price=form.cleaned_data['price'],
                total_price=form.cleaned_data['total_price'],
                client=current_client
            )
            return redirect('history/')
    else:
        form = FuelQuoteForm()

    return render(request, 'fuel_quote.html', {
        'form': form, 
        'current_client': current_client, 
        'quote_count': quote_count
    })



@login_required
def history(request):
    
    current_client = client.objects.get(client=request.user)
    
    
    fuel_quotes = FuelQuote.objects.filter(client=current_client).order_by('-id')
    
    return render(request, 'fuelQuoteHistory.html', {
        'fuel_quotes': fuel_quotes
    })
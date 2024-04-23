from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import FuelQuote
from .forms import FuelQuoteForm
from profile.models import client
from price.models import Pricing  
from django.contrib.auth.decorators import login_required

@login_required
def quote(request):
    current_client = client.objects.get(client=request.user)
    quote_count = FuelQuote.objects.filter(client=current_client).count()
    form = FuelQuoteForm(request.POST or None)
    suggested_price = None
    total_amount_due = None

    if request.method == 'POST' and form.is_valid():
        if 'get_quote' in request.POST:

            pricing = Pricing(
                location=current_client.state,
                rate_history=quote_count > 0,
                gallons=form.cleaned_data['gallons'],
            )
            suggested_price, total_amount_due = pricing.calculate_price()
                
            form = FuelQuoteForm(initial={
                'gallons': form.cleaned_data['gallons'],
                'date': form.cleaned_data['date'],
                'price': suggested_price,
                'total_price': total_amount_due,
                })
                
        else:
            FuelQuote.objects.create(
                gallons=form.cleaned_data['gallons'],
                address=current_client.address1,
                date=form.cleaned_data['date'],
                price=form.cleaned_data['price'],
                total_price=form.cleaned_data['total_price'],
                client=current_client
            )       
            return redirect('history/')
       

    return render(request, 'fuel_quote.html', {
        'form': form,
        'current_client': current_client,
        'quote_count': quote_count,
        'suggested_price': suggested_price,
        'total_amount_due': total_amount_due
    })

@login_required
def history(request):
    current_client = client.objects.get(client=request.user)
    fuel_quotes = FuelQuote.objects.filter(client=current_client).order_by('-id')
    
    return render(request, 'fuelQuoteHistory.html', {
        'fuel_quotes': fuel_quotes
    })
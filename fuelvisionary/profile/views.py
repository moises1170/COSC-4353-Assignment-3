from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import client
from django.contrib.auth.decorators import login_required



@login_required
def userPage(request):
    
    
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        state = request.POST.get("state")
        city = request.POST.get("city")
        zipcode =request.POST.get("zipcode")
        user = request.user

        # Check if the user is authenticated (logged in)
        if user.is_authenticated:
            # Create a new client instance associated with the logged-in user
            new_client = client.objects.create(fullName=fullname, address1=address1, address2=address2, state=state, city=city, zipcode=zipcode, client=user)

            return redirect('home')
        else:
            # Handle the case where the user is not authenticated
            return HttpResponse('User is not authenticated', status=401)
    else:
        return render(request, 'client-profile.html')
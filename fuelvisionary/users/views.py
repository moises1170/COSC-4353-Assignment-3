from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from profile.models import client
from django.contrib.auth import authenticate, login, logout


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                client_instance = client.objects.get(client=user)
                return redirect('home')
            except:
                return redirect('management')
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'login.html')


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate form data
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')

    return render(request, 'register.html')


@login_required
def homePage(request):
    user = request.user
    if user.is_authenticated:
        client_instance = client.objects.get(client=user)
    else:
        # Handle the case where the user is not authenticated
        return HttpResponse('User is not authenticated', status=401)

    context = {
        'client_instance': client_instance
    }
    return render(request, 'home.html',context)



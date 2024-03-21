from django.shortcuts import render
from django.http import HttpResponse
from .models import client

def userPage(request):
    return render(request, 'client-profile.html')

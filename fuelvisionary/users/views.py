from django.shortcuts import render
from django.http import HttpResponse

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')
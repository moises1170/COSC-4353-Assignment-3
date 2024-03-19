from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage),
    path('register/', views.registerPage, name = 'register')
]


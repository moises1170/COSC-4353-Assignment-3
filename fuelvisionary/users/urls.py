from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name ="register"),
    path('home/', views.homePage, name="home"),
]


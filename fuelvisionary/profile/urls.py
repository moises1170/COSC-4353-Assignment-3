from django.urls import path
from . import views

urlpatterns = [
    path('management/', views.userPage, name='management')
]

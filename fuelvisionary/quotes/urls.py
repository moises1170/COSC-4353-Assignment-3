from django.urls import path
from . import views

urlpatterns = [
    path('fuelquote/', views.fuelQuote, name='fuelquote'),
    path('quotehistory/', views.quoteHistory, name='quotehistory')
]
from django.urls import path
from . import views

urlpatterns = [
    path('fuelquote/', views.quote, name='fuelquote'),
    path('fuelquote/history/', views.history, name='quotehistory'),
]
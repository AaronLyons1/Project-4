from django.urls import path
from .views import booking

app_name = 'reservation'

urlpatterns = [
    path('user/', booking.as_view(), name='booking')
]

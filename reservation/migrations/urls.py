from django.urls import path
from .views import booking

app_name = 'restruant'

urlpatterns = [
    path('bookings/', booking.as_view(), name='bookings')
]
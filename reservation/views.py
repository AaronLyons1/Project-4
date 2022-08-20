from django.shortcuts import render
from .views import user


class booking(ListView):
    model = user

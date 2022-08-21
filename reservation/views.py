from django.shortcuts import render, ListView
from .models import user


class booking(ListView):
    model = user

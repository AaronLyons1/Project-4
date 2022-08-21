from django.shortcuts import render
from .models import user


class booking(ListView):
    model = user

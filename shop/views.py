# shop/views.py
from django.shortcuts import render
from .models import Website

def shop(request):
    websites = Website.objects.all()
    return render(request, 'shop.html', {'websites': websites})
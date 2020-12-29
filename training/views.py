
from django.shortcuts import render

def about(request):
    return render(request, 'This is about page')

def home(request):
    return render(request, 'home.html')
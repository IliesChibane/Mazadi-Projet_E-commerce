from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'inscription.html')

def signup(request):
    return render(request, 'sinup.html')

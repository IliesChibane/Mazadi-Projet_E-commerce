from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'inscription.html')

def signup(request):
    return render(request, 'sinup.html')

def article(request):
    return render(request, "article.html")

def categories(request):
    return render(request ,"categories.html")

def categories2(request):
    return render(request ,"categories2.html")

def details(request):
    return render(request ,"details.html")

def encheres(request):
    return render(request ,"encheres.html")

def encheries(request):
    return render(request ,"encheries.html")

def home_user(request):
    return render(request ,"index2.html")

def meubles(request):
    return render(request ,"meubles.html")

def profile(request):
    return render(request ,"profile.html")

def sport(request):
    return render(request ,"sport.html")

def telephones(request):
    return render(request ,"telephones.html")

def voitures(request):
    return render(request ,"voitures.html")
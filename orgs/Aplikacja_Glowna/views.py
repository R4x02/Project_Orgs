from django.shortcuts import render
from .models import Uzytkownik

def main(request):
    UZYTKOWNIK = Uzytkownik.objects.count()
    return render(request, 'index.html', {'ilosc_uzytkownikow': UZYTKOWNIK})
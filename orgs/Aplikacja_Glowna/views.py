from django.shortcuts import render
from .models import Wizyta, Pacjent

def main(request):
    WIZYTY = Wizyta.objects.count()
    PACJENCI = Pacjent.objects.all()
    return render(request, 'index.html', {'ilosc_wizyt': WIZYTY, 'pacjenci': PACJENCI})
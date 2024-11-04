from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Pacjent(models.Model):
    Nazwisko = models.CharField(max_length=100)
    Imie = models.CharField(max_length=100)
    Miasto = models.CharField(max_length=100, default='Białystok')
    Ulica = models.CharField(max_length=100)
    Wiek = models.IntegerField()

    def __str__(self):
        return f"{self.Imie} {self.Nazwisko}"

class Wizyta(models.Model):
    Data = models.DateField()
    Zalecenia = models.TextField()
    pacjent_klucz_obcy = models.ForeignKey(Pacjent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Data} {self.pacjent_klucz_obcy.Nazwisko}"
from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Uzytkownik(models.Model):
    Imie = models.CharField(max_length=100)
    Nazwisko = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Imie} {self.Nazwisko}"




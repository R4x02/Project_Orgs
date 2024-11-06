from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.db.models import ForeignKey

def generate_team_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


# Create your models here.
class Uzytkownik(models.Model):
    Imie = models.CharField(max_length=100)
    Nazwisko = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Imie} {self.Nazwisko}"

class Team(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_teams')
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name


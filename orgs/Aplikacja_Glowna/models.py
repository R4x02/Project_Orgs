from django.db import models
from django.contrib.auth.models import User
import random
import string

# Model użytkownika
class Uzytkownik(models.Model):
    Imie = models.CharField(max_length=100)
    Nazwisko = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Imie} {self.Nazwisko}"

# Funkcja generująca unikalny kod zespołu
def generate_team_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Model zespołu
class Team(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default=generate_team_code)  # Dodanie domyślnego generatora kodów
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_teams')
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name="messages", on_delete=models.CASCADE)  # relacja z zespołem
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content}"
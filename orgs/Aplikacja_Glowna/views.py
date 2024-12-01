from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
from .forms import *

def custom_logout(request):
    logout(request)
    return redirect('main')

def profile_redirect(request):
    return redirect('orgs/')

def main(request):
    if request.user.is_authenticated:
        teams = Team.objects.filter(members=request.user) | Team.objects.filter(owner=request.user)
        return render(request, 'index.html', {'teams': teams})
    else:
        return redirect('login')

def info(request):
    if request.method == 'POST':
        name = request.POST.get('Imie')
        lastname = request.POST.get('Nazwisko')
        email = request.POST.get('Gmail')

        if name and lastname and email:
            uzytkownik = Uzytkownik.objects.create(Imie=name, Nazwisko=lastname, gmail=email)
            return redirect('main')
        else:
            messages.error(request, 'Wszystkie pola są wymagane!')

    return render(request, 'info.html')


@login_required
def join_team(request):
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            kod = form.cleaned_data['code']
            try:
                zespol = Team.objects.get(code=kod)
                zespol.members.add(request.user)
                messages.success(request, 'Pomyślnie dołączono do zespołu!')
                return redirect('team_detail', team_id=zespol.id)
            except Team.DoesNotExist:
                messages.error(request, 'Zespół o podanym kodzie nie istnieje.')
    else:
        form = JoinTeamForm()
    return render(request, 'join_team.html', {'form': form})

@login_required
def team_detail(request, team_id):
    zespol = get_object_or_404(Team, id=team_id)
    return render(request, 'team_detail.html', {'team': zespol})

@login_required
def add_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        if team_name:
            if Team.objects.filter(name=team_name, owner=request.user).exists():
                messages.error(request, f"Zespół '{team_name}' już istnieje!")
            else:
                Team.objects.create(name=team_name, owner=request.user)
                messages.success(request, f"Zespół '{team_name}' został pomyślnie dodany!")
        else:
            messages.error(request, "Nie udało się dodać zespołu. Spróbuj ponownie.")
        return redirect('main')  # Powrót na stronę główną
    return render(request, 'add_team.html')

@login_required
def delete_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        try:
            team = Team.objects.get(name=team_name, owner=request.user)
            team.delete()
            messages.success(request, f"Zespół '{team_name}' został usunięty!")
        except Team.DoesNotExist:
            messages.error(request, f"Zespół '{team_name}' nie istnieje")
        return redirect('main')  # Powrót na stronę główną
    return render(request, 'delete_team.html')


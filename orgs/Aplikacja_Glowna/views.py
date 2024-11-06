from django.shortcuts import render
from .models import Uzytkownik
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Team
from .forms import JoinTeamForm

def main(request):
    UZYTKOWNIK = Uzytkownik.objects.count()
    return render(request, 'index.html', {'ilosc_uzytkownikow': UZYTKOWNIK})

@login_required
def join_team(request):
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                team = Team.objects.get(code=code)
                team.members.add(request.user)
                messages.success(request, 'Successfully joined the team!')
                return redirect('team_detail', team_id=team.id)
            except Team.DoesNotExist:
                messages.error(request, 'Team with this code does not exist.')
    else:
        form = JoinTeamForm()
    return render(request, 'join_team.html', {'form': form})

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'team_detail.html', {'team': team})

@login_required
def add_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        if team_name:
            Team.objects.create(name=team_name, owner=request.user)
        return redirect('main')  # Powrót na główną stronę
    return render(request, 'add_team.html')  # Szablon nie jest wymagany, jeśli dodajemy zespoły z tej samej strony
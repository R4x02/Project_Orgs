from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.exceptions import PermissionDenied
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

@login_required
def info(request):
    # Sprawdzenie, czy użytkownik już wypełnił dane
    if Uzytkownik.objects.filter(id=request.user.id).exists():
        return redirect('main')  # Przekierowanie na stronę główną, jeśli dane już istnieją

    if request.method == 'POST':
        name = request.POST.get('Imie')
        lastname = request.POST.get('Nazwisko')
        email = request.POST.get('Gmail')

        if name and lastname and email:
            # Tworzenie rekordu użytkownika
            Uzytkownik.objects.create(
                Imie=name,
                Nazwisko=lastname,
                gmail=email
            )
            messages.success(request, "Twoje dane zostały zapisane.")
            return redirect('main')
        else:
            messages.error(request, 'Wszystkie pola są wymagane!')

    return render(request, 'info.html')

@login_required
def join_team (request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            druzyna = Team.objects.get(code=code)
            druzyna.members.add(request.user)
            messages.success(request, f"Dołączyłeś do zespołu: {druzyna.name}")
            return redirect('team_detail', team_id=druzyna.id)  # Przekierowanie na szczegóły drużyny
        except Team.DoesNotExist:
            messages.error(request, "Zespół o podanym kodzie nie istnieje.")
            return redirect('index.html')

    return render(request, 'team_detail.html')


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    messages = team.messages.all().order_by('timestamp')

    return render(request, 'team_detail.html', {
        'team': team,
        'messages': messages,
    })

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

@login_required
def team_chat(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.user not in team.members.all() and request.user != team.owner:
        raise PermissionDenied("Nie masz dostępu do tego czatu.")

    messages = team.messages.order_by('timestamp')
    return render(request, 'team_chat.html', {'team': team, 'messages': messages})


@csrf_exempt
@login_required
def send_message(request, team_id):
    if request.method == 'POST':
        team = get_object_or_404(Team, id=team_id)
        if request.user not in team.members.all() and request.user != team.owner:
            return JsonResponse({'error': 'Brak dostępu.'}, status=403)

        content = request.POST.get('content')
        if content:
            message = ChatMessage.objects.create(team=team, user=request.user, content=content)

            # Konwertowanie timestamp do lokalnej strefy czasowej
            local_timestamp = timezone.localtime(message.timestamp)
            return JsonResponse({'user': message.user.username, 'content': message.content,
                                 'timestamp': local_timestamp.strftime('%Y-%m-%d %H:%M:%S')})
        return JsonResponse({'error': 'Treść wiadomości jest wymagana.'}, status=400)
    return JsonResponse({'error': 'Nieobsługiwana metoda.'}, status=405)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
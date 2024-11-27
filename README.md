# Project_Orgs
** NOWE REPO ** 
 
~~ https://github.com/MaciejMocarski/Project_Orgs ~~

Project_Orgs

### Zmiany 17.11.2024:

#### Templatki:

* dodanie templatki add_team.html (obsługiwanie dodawania nowych teamów)
* dodanie templatki base.html (baza dla strony)
* dodanie templatki login.html (logowanie się)
* zmiana templatki index.html (teraz extenduje base.html zamiast być domyślną templatką)

#### Modele:

* Brak zmian, git po prostu lubi mieć świra na punkcie indentów

### urls.py:

* dodanie urls logout, który obsługuje ścięzkę, słuzącą do wylogowania uzytkownika
* dodanie urls login, który obsługuje ścięzkę, słuzącą do logowania uzytkownika

#### Migracje:

* Dodanie nowych migracji :D

#### Widoki (•᷄- •᷅ ;): 

* Dojście do wniosku, ze widoki to dzieło szatana
* def custom_logout, profile_redirect - widoki które obsługują redirecty dzięki którym Django nie wywala nas na jakieś anomalie tylko od razu na pozadana strone
* main - aktualizacja widoku w celu obslugi logowania
* join_team - views w wersji beta, którego przy okazji ugotował chat jak prosiłem go o pomoc z czymś innym pozdro
* team_detail - to samo co join_team, przyda się w przyszłości
* add_team - zmiany dzięki, którym w końcu mona dodać zespół :D

#### Style:
* Lekka zabawa css, tylko zeby dojść do wniosku, ze nie dziala (MACIEJU NAPRAW)


#### INNE BARDZO WAŻNE RZECZY:

* Wszystko co strona umozliwia zrobic dziala. Jednak trzeba pamietać, ze przy dodawaniu funkcji mozna cos zepsuć ;)
* Dodanie usera testowego: testuser, haslo testpassword
* Dodanie usera admina: sigma, haslo Ohio (to chyba nie powinna byc informacja publiczna)
* Jezeli coś nie działa, to z winny Zawadzkiego

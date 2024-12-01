# Project_Orgs
Project_Orgs
### Zmiany 30.11.2024 i  01.12.2024:

#### Views:
* Po zalogowaniu trzeba podać swoje dane które są zapisywane w models
* Wykorzystujemy kod danego zespołu, dodalem go w html

#### Style:
* Ciężkie zmiany css'a
* Nowy styl dark mode'a
* Zmieniono kolory czcionek i wielkości przycisków dla dostępności
* Ogólnie sporo się nauczyłem o wyglądzie

#### settings.py:
* Poprawiono strefę czasową ('Europe/Warsaw' zamiast 'UTC')

### Zmiany 29.11.2024:

#### Views:
* Dodane funkcje usuwającą drużynę
* Przy dodawaniu drużyn sprawdza czy już taka nie istnieje

#### Templatki:
* Zmiana index.html
* Dodanie delete_team.html
* W loginie próbuje dodać zmienne z modułu

#### Moduły
* Próbuje wykorzystać moduły bo jak na razie to leżą i kwiczą


### Zmiany 27.11.2024:

#### Style:
* Podłączanie trochę zajeło, ale się udało:
* Naprawiono 404 styles.css
* Zmiana koloru wyświetlania hyperlinków
* poprawiono wygląd głównej strony

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

* Dojście do wniosku, ze widoki to dzieło szatana (SPOKOJNIE NAPRAWIAM)
* def custom_logout, profile_redirect - widoki które obsługują redirecty dzięki którym Django nie wywala nas na jakieś anomalie tylko od razu na pozadana strone
* main - aktualizacja widoku w celu obslugi logowania
* join_team - views w wersji beta, którego przy okazji ugotował chat jak prosiłem go o pomoc z czymś innym pozdro
* team_detail - to samo co join_team, przyda się w przyszłości
* add_team - zmiany dzięki, którym w końcu mona dodać zespół :D

#### Style:
* Lekka zabawa css, tylko zeby dojść do wniosku, ze nie dziala (MACIEJU NAPRAW) (NAPRAWIONE) (WALE GITHUBA ALE NAPRAWIONE)


#### INNE BARDZO WAŻNE RZECZY:

* Wszystko co strona umozliwia zrobic dziala. Jednak trzeba pamietać, ze przy dodawaniu funkcji mozna cos zepsuć ;)
* Dodanie usera testowego: testuser, haslo testpassword
* Dodanie usera admina: sigma, haslo Ohio (to chyba nie powinna byc informacja publiczna)
* Jezeli coś nie działa, to z winny Zawadzkiego

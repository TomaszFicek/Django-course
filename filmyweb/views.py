from django.shortcuts import render

from django.http import HttpResponse

from .models import Film
from .forms import MovieForm

def pierwsza_strona(request): # definicja funkcji do wyświetlenia strony http

    # return HttpResponse("<h1>to jest nasz pierwszy test<h1/>") # HttpResponse jest to metoda do wyświetlenia zwykłego
    #.. napisu na stronie

    wszystkie = Film.objects.all() # przypisanie do zmiennej "wszytskie" klasy "Film", którą utworzylismy w pliku
    # "models.py" -> klasa ta to obiekt która twarzy baze danych z filmami -> metoda "objects.all" pozwala na dostep
    # do wszytskich elementow bazy danych "db.sqlite3"
    return render(request, 'filmy.html', {'filmy': wszystkie}) # motoda RENDER słuzy do dodawania na stronę
    #   templejtow (stron w HTMLu) - w naszym przypadku "filmy.html" -> po przecinku dodano obiekt (obiekt nazwano "filmy")
    #  z zawartoscią bazy danch (przypisany do zmiennej "wszytskie"), w pliku "filmy.html" wprowadzono skladnię, która
    # przedatawia wyswietlenie tej bazy danych

def nowy_film(request):
    form = MovieForm(request.POST or None, request.FILES or None) # przypisanie do zmiennej "form" klasy "MovieForm"
    # za pomocą której są wysyłane dane do bazy danych - przy pomocy "request.POST" są wysyłąne dane do bazy danych,
    # a za pomocą "request. FILES" są wysyłane media do BD , na przykład zjęcia dołączne do filmów

    if form.is_valid(): # warunek sprawdzjacy czy powyzej zapisane dane są odpowiednie/dobrego typu jak "fields" w BD
        form.save() # jezeli powyzszy warunek spełniony to dane sa zapisywane do BD
    return render(request, 'nowy_film.html', {'form': form}) # "Funkcja render() bierze obiekt request jako swój
    #  pierwszy argument, nazwę szablonu jako drugi argument i słownik jako swój opcjonalny trzeci argument. Zwraca
    #  obiekt HttpResponse danego szablonu wyrenderowany z danym kontekstem - czyli ponownie wracamy do strony z
    #  formularzem "nowy_film.http"

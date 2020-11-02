from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import MovieForm
from django.contrib.auth.decorators import login_required # zaimportowanie dekoratora do wymagania logowania sie -
# wstawiamy ten dekorator przed funkcją, do której chcemy aby dostep mili tylko zalogowani uzytkownicy


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

@login_required() # dodanie dekoratora do poniżej funkcji
def nowy_film(request):
    form = MovieForm(request.POST or None, request.FILES or None) # przypisanie do zmiennej "form" klasy "MovieForm"
    # za pomocą której są wysyłane dane do bazy danych - przy pomocy "request.POST" są wysyłąne dane do bazy danych,
    # a za pomocą "request. FILES" są wysyłane media do BD , na przykład zjęcia dołączne do filmów

    if form.is_valid(): # warunek sprawdzjacy czy powyzej zapisane dane są odpowiednie/dobrego typu jak "fields" w BD
        form.save() # jezeli powyzszy warunek spełniony to dane sa zapisywane do BD
        return redirect(pierwsza_strona) # metoda "redirect" pozwala na przejście do funkcji podanej w argumencie - w
        # praktyce to będzie tak wyglądało, że jeżeli "form" jest poprawny, zostanie on zapisany a potem metoda
        # "redirect" zabierze nas na stronę ze wszystkimi filmami

    return render(request, 'film_form.html', {'form': form, 'nowy': True}) # "Funkcja render() bierze obiekt request jako swój
    #  pierwszy argument, nazwę szablonu jako drugi argument i słownik jako swój opcjonalny trzeci argument ( w
    # słowniku wstawiamy argumenty przesyłane do szablonu "film_form.html" - parametr "nowy" słyży do sprawdzania
    # czy dodajemy nowy film czy edytujemy instniejący za pomocą jednego szablonu "film_form". Zwraca
    #  obiekt HttpResponse danego szablonu wyrenderowany z danym kontekstem - czyli ponownie wracamy do strony z
    #  formularzem "nowy_film.http"

@login_required()
def edytuj_film(request, id): #definicja funkcji do edytowania filmu - w argumencie podajemy id filmu który chcemy edyto
    film = get_object_or_404(Film, pk=id) # do zmiennej "fil" przypsujemy metodę do pobierania objektu (filmu) z bazy
    # danych -  w przypadku podania filmu,który nie istnieje, metoda ta wyrzuca błąd 404

    # gdy do zmiennej "film" został przypisany obiekt/film, który będzie edytowany - można zastosować skrypt, który był
    # używany tworzenia nowych rekordów w bazie danych ( skrypt z funkcji "nowy"film"), z takim wyjątkiem, ze należy
    # dopisać w parametrze zmienną "film" do której przypisany jest wybrany film do edycji

    form = MovieForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(pierwsza_strona)

    return render(request, 'film_form.html', {'form': form, 'nowy': False})

@login_required()
def usun_film(request, id): #definicja funkcji do edytowania filmu - w argumencie podajemy id filmu który chcemy edyto
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(pierwsza_strona)

    return render(request, 'potwierdz.html', {'film': film})
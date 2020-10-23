from django.shortcuts import render

from django.http import HttpResponse

from .models import Film

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

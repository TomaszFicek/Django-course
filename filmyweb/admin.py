from django.contrib import admin
from .models import Film

# admin.site.register(Film) # rejestracja (zamieszczenie w aplikacji "filmyweb") utworzonych w pliku "models.py",
# w class "Film", st    worzonych tam wszytskich FIELDS

@admin.register(Film) # inny sposón zarejestrowania FIELDS z class "Film" - w class poniżej stosuje się różne parametry
class FilmAdmin(admin.ModelAdmin):
    #fields = ["tytul", "opis"] # parametr "fields" służy do określenia, które FIELDS chcemy zastosować w aplikacji - w
    # .. tym przypadku tytul i opis
    #exclude = ["opis"] # EXCLUDE służy do włączenia wszytkich FIELDS poza zamieszczoną w argumencie tej metody
    list_display = ["tytul", "rok", "imbd_rating"] #metoda ta sluzy do zrobienia listy, której klumnami są argumenty tej
    #.. tej metody - liste mozna sortowac maljaco/rosnaco na tyh kolumnach
    list_filter = ["rok"] # wstawianie mozliwosci filtrowania listy po FIELDS zamieszczonym w nawiasie
    search_fields = ["tytul", "opis"] # wstawenie mozliwosci wyszukiwania w liscie fimów po FIELDS zamieszczonych w []



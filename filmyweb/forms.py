#plik do tworzenia formularzy, które będą przesyłac dane do bazy danych - zapisywanie nwych filmów przez uzytkowników

from django.forms import ModelForm # metoda do tworzenia formularzy
from .models import Film

class MovieForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'opis', 'premiera', 'rok', 'imbd_rating', 'plakat']

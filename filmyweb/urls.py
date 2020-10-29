from django.urls import path
from filmyweb.views import pierwsza_strona, nowy_film, edytuj_film, usun_film

urlpatterns = [

    path ('wszystkie/', pierwsza_strona, name='pierwsza_strona'), # podanie adresu URL do stron http zdefiniowanych w pliku "views.py"
    path('nowy/', nowy_film, name='nowy_film'),
    path('edytuj/<int:id>/', edytuj_film, name='edytuj_film'), # w argumencie "path" musimy podać który chcemy
    #  film edytować, dlatego musimy zamieścić jego "id" - parametr "name" przechwouje nazwe URL gdzie jest funkcja do
    #  edycji filmow - jako URL będzie podany id edytowanego filmu w formacie int

    path('usun/<int:id>/', usun_film, name='usun_film')

]

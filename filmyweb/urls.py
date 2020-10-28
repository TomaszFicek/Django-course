from django.urls import path
from filmyweb.views import pierwsza_strona, nowy_film

urlpatterns = [

    path ('wszystkie/', pierwsza_strona), # podanie adresu URL do stron http zdefiniowanych w pliku "views.py"
    path('nowy/', nowy_film),

]

from django.urls import path
from filmyweb.views import pierwsza_strona

urlpatterns = [

    path ('test/', pierwsza_strona) # podanie adresu URL do stron http zdefiniowanych w pliku "views.py"
]

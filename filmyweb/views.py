from django.shortcuts import render

from django.http import HttpResponse
import datetime

def pierwsza_strona(request): # definicja funkcji do wyświetlenia strony http

    return HttpResponse("<h1>to jest nasz pierwszy test<h1/>")



def aktualny_czas(request): #definicja funkcji do wuświetlenia strony z aktulanym czasem
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
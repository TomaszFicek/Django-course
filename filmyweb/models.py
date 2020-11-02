from django.db import models

class DodatkoweInfo(models.Model):

    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Drama'),
    }

    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)

class Film(models.Model): # klasa w ktorej zamieszczomy rozne FIELDS
    tytul = models.CharField(max_length=64, unique=True,)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default='')
    premiera = models.DateField(null=True, blank=True)
    imbd_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True) # wstawienie
    # dodatkowe "fields" do modelu....
    # ... "Film" - jest do fields "zabrane" z innego modelu "DodatkoweInfo" za pomocą relacji "jeden do jeden" (metoda
    # "OneToOneField" - jaki parametry metody podajemy z jakiego modelu bierzemy fields , a parametr "on-delete"
    # służy do poinformowania co się stanie z modelem "DodatkoweInfo" w momencie usunięcia modelu "Film" - metoda
    #  "models.CASCADE" powoduje usunięcie modelu "DodatkoweInfo" w momencie usunięcia modelu "Film"


    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)



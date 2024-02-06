import random
from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Korisnik , Kategorija, Proizvod, Narudzba, Placanje
from main.factory import KorisnikFactory, KategorijaFactory, ProizvodFactory, NarudzbaFactory, PlacanjeFactory

BROJ_KORISNIKA = 10
BROJ_KATEGORIJA = 10
BROJ_PROIZVODA = 50
BROJ_NARUDZBI = 20
BROJ_PLACANJA = 20

class Command(BaseCommand):
    help = "Generira testne podatke"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Brisanje starih podataka...")
        modeli = [Korisnik, Kategorija, Proizvod, Narudzba, Placanje]
        for model in modeli:
            model.objects.all().delete()

        self.stdout.write("Stvaranje novih podataka...")

        for _ in range(BROJ_KORISNIKA):
            korisnik = KorisnikFactory()
         
        for _ in range(BROJ_KATEGORIJA):
            kategorija = KategorijaFactory()

        for _ in range(BROJ_PROIZVODA):
            proizvod = ProizvodFactory()

        for _ in range(BROJ_NARUDZBI):
            narudzba = NarudzbaFactory()

        for _ in range(BROJ_PLACANJA):
            placanje = PlacanjeFactory()
  

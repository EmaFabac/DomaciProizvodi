import factory
from factory.django import DjangoModelFactory
from faker import Faker
from main.models import Korisnik, Kategorija, Proizvod, Narudzba, Placanje
import random
from django.utils import timezone  # Dodaj ovu liniju

fake = Faker()

class KorisnikFactory(DjangoModelFactory):
    class Meta:
        model = Korisnik

    ime_korisnika = factory.LazyAttribute(lambda x: fake.first_name())
    prezime_korisnika = factory.LazyAttribute(lambda x: fake.last_name())
    adresa_korisnika = factory.LazyAttribute(lambda x: fake.street_address())
    mobitel_korisnika = factory.LazyAttribute(lambda x: fake.random_number(digits=10))
    email_korisnika = factory.LazyAttribute(lambda x: fake.email())

class KategorijaFactory(DjangoModelFactory):
    class Meta:
        model = Kategorija

    id_kategorije = factory.LazyFunction(lambda: str(random.randint(10000, 99999)))
    naziv_kategorije = factory.LazyAttribute(lambda x: fake.word())

class ProizvodFactory(DjangoModelFactory):
    class Meta:
        model = Proizvod

    id_proizvoda = factory.LazyFunction(lambda: str(random.randint(10000, 99999)))
    naziv_proizvoda = factory.LazyAttribute(lambda x: fake.word())
    cijena_proizvoda = factory.LazyAttribute(lambda x: random.randint(1, 100))
    opis_proizvoda = factory.LazyAttribute(lambda x: fake.text())
    slika_proizvoda = factory.LazyAttribute(lambda x: fake.image_url())
    proizvod_kategorija = factory.SubFactory(KategorijaFactory)
    proizvod_korisnik = factory.SubFactory(KorisnikFactory)

class NarudzbaFactory(DjangoModelFactory):
    class Meta:
        model = Narudzba

    id_narudzbe = factory.LazyFunction(lambda: str(random.randint(10000, 99999)))
    ukupna_cijena = factory.LazyAttribute(lambda x: random.randint(1, 1000))
    narudzba_korisnik = factory.SubFactory(KorisnikFactory)

class PlacanjeFactory(DjangoModelFactory):
    class Meta:
        model = Placanje

    narudzba = factory.SubFactory(NarudzbaFactory)  # Zamijeni s pravilnim putem do NarudzbaFactory
    broj_kartice = fake.credit_card_number()
    ime_kupca = fake.first_name()
    prezime_kupca = fake.last_name()
    vrijeme_placanja = fake.date_time_this_decade(tzinfo=timezone.utc)  # Ovdje dodano tzinfo


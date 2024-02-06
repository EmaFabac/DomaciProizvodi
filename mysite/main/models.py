from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Korisnik(models.Model):
    ime_korisnika = models.CharField(max_length=100)
    prezime_korisnika = models.CharField(max_length=100)
    adresa_korisnika = models.CharField(max_length=100)
    mobitel_korisnika = models.CharField(max_length=10)
    email_korisnika = models.EmailField()
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.email_korisnika
    
class Kategorija(models.Model):
    id_kategorije = models.CharField(max_length=5)
    naziv_kategorije = models.CharField(max_length=100)
    def __str__(self):
        return self.id_kategorije

class Proizvod(models.Model):
    id_proizvoda = models.CharField(max_length=5)
    naziv_proizvoda = models.CharField(max_length=100)
    cijena_proizvoda = models.IntegerField()
    opis_proizvoda = models.TextField()
    slika_proizvoda = models.ImageField(null=True, blank=True, upload_to="images/")
    proizvod_kategorija = models.ForeignKey(Kategorija, related_name='proizvodi', on_delete=models.CASCADE)
    proizvod_korisnik = models.ForeignKey(Korisnik,default=1, on_delete=models.CASCADE)


    def __str__(self):
        return self.id_proizvoda

class Narudzba(models.Model):
    id_narudzbe = models.AutoField(primary_key=True)
    ukupna_cijena = models.IntegerField()
    narudzba_proizvod = models.ManyToManyField(Proizvod)
    narudzba_korisnik = models.ForeignKey(Korisnik,null=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"Order {self.id_narudzbe}"
    
class Placanje(models.Model):
    narudzba = models.OneToOneField(
        Narudzba,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    broj_kartice = models.CharField(max_length=20)
    ime_kupca= models.CharField(max_length=100)
    prezime_kupca = models.CharField(max_length=100)
    vrijeme_placanja= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.broj_kartice
        

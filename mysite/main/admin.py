from django.contrib import admin
from .models import *

model_list = [Korisnik, Placanje, Narudzba, Proizvod, Kategorija]
admin.site.register(model_list)
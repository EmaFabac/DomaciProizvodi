from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *
from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from main.models import *
from main.views import *
from django.apps import apps

from .cart import Cart


class TestMainUrls(SimpleTestCase):

    def test_landing_url_is_resolved(self):
        url = reverse('main:landing')
        self.assertEquals(resolve(url).func.view_class, LandingPageView)

    def test_search_results_url_is_resolved(self):
        url = reverse('main:search_results')
        self.assertEquals(resolve(url).func.view_class, SearchResultsView)

    def test_about_us_url_is_resolved(self):
        url = reverse('main:about_us')
        self.assertEquals(resolve(url).func.view_class, AboutUsView)

    def test_detalji_kategorije_url_is_resolved(self):
        url = reverse('main:detalji_kategorije', args=[43071])  # assuming you pass some valid category id
        self.assertEquals(resolve(url).func, detalji_kategorije)

    def test_pretrazi_proizvode_url_is_resolved(self):
        url = reverse('main:pretrazi_proizvode')
        self.assertEquals(resolve(url).func, pretrazi_proizvode)

    def test_login_url_is_resolved(self):
        url = reverse('main:login')
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_url_is_resolved(self):
        url = reverse('main:logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_register_url_is_resolved(self):
        url = reverse('main:register')
        self.assertEquals(resolve(url).func, register)

    def test_profile_url_is_resolved(self):
        url = reverse('main:profile')
        self.assertEquals(resolve(url).func.view_class, profile)

    def test_mojiproizvodi_url_is_resolved(self):
        url = reverse('main:mojiproizvodi')
        self.assertEquals(resolve(url).func.view_class, mojiproizvodi)

    def test_update_url_is_resolved(self):
        url = reverse('main:update', args=[99152])  # assuming you pass some valid proizvodi id
        self.assertEquals(resolve(url).func.view_class, ProizvodeUpdate)

    def test_delete_url_is_resolved(self):
        url = reverse('main:delete', args=[72886])  # assuming you pass some valid proizvodi id
        self.assertEquals(resolve(url).func.view_class, ProizvodeDelete)

    def test_add_proiz_url_is_resolved(self):
        url = reverse('main:add')
        self.assertEquals(resolve(url).func, add_proiz)

    def test_cart_summary_url_is_resolved(self):
        url = reverse('main:cart_summary')
        self.assertEquals(resolve(url).func, cart_summary)

    def test_cart_add_url_is_resolved(self):
        url = reverse('main:cart_add')
        self.assertEquals(resolve(url).func, cart_add)

    def test_cart_delete_url_is_resolved(self):
        url = reverse('main:cart_delete')
        self.assertEquals(resolve(url).func, cart_delete)

    def test_submit_order_url_is_resolved(self):
        url = reverse('main:sumbite_order')
        self.assertEquals(resolve(url).func, submit_order)

    def test_popis_url_is_resolved(self):
        url = reverse('main:popis')
        self.assertEquals(resolve(url).func.view_class, NarudzbaPopis)

    def test_placanje_url_is_resolved(self):
        url = reverse('main:palcanje', args=[99379])  # assuming you pass some valid narudzba_id
        self.assertEquals(resolve(url).func.view_class, Placanje)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('main:landing')
        self.search_results_url = reverse('main:search_results')
        self.about_us_url = reverse('main:about_us')
        self.detalji_kategorije_url = reverse('main:detalji_kategorije', args=[48735])  # Ovdje stavite valjani ID kategorije
        self.pretrazi_proizvode_url = reverse('main:pretrazi_proizvode')
        self.login_url = reverse('main:login')
        self.logout_url = reverse('main:logout')
        self.register_url = reverse('main:register')
        self.profile_url = reverse('main:profile')
        self.mojiproizvodi_url = reverse('main:mojiproizvodi')
        self.popis_url = reverse('main:popis')
        self.placanje_url = reverse('main:palcanje', args=[99378])  # Ovdje stavite valjani ID narudžbe
        self.add_proiz_url = reverse('main:add')
        self.cart_summary_url = reverse('main:cart_summary')
        self.cart_add_url = reverse('main:cart_add')
        self.cart_delete_url = reverse('main:cart_delete')
        self.submit_order_url = reverse('main:sumbite_order')

    def test_project_homepage_GET(self):
        response = self.client.get(self.homepage_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

    def test_search_results_GET(self):
        response = self.client.get(self.search_results_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

    def test_about_us_GET(self):
        response = self.client.get(self.about_us_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'o_nama.html')

    def test_detalji_kategorije_url_is_resolved(self):
        # Provjerite je li URL za detalje kategorije ispravno rezoluiran
        url = reverse('main:detalji_kategorije', args=[48735])  # Zamijenite 1 s valjanim ID-om kategorije
        self.assertEquals(resolve(url).func, detalji_kategorije)
 
    def test_pretrazi_proizvode_GET(self):
        response = self.client.get(self.pretrazi_proizvode_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pretraga.html')

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)  # Redirects to landing page

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_mojiproizvodi_GET(self):
        response = self.client.get(self.mojiproizvodi_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mojiproizvodi.html')

    def test_popis_GET(self):
        response = self.client.get(self.popis_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mojanarudzba.html')


    def test_add_proiz_GET(self):
        response = self.client.get(self.add_proiz_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_proizvode.html')

    def test_cart_summary_GET(self):
        response = self.client.get(self.cart_summary_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/mojenarudzbe.html')




class TestModels(TestCase):
    def setUp(self):
        self.Korisnik = apps.get_model('main', 'Korisnik')
        self.Kategorija = apps.get_model('main', 'Kategorija')
        self.Proizvod = apps.get_model('main', 'Proizvod')
        self.Narudzba = apps.get_model('main', 'Narudzba')
        self.Placanje = apps.get_model('main', 'Placanje')

        self.korisnik1 = self.Korisnik.objects.create(
            ime_korisnika='Test Ime',
            prezime_korisnika='Test Prezime',
            adresa_korisnika='Test Adresa',
            mobitel_korisnika='1234567890',
            email_korisnika='test@example.com'
        )

        self.kategorija1 = self.Kategorija.objects.create(
            id_kategorije='001',
            naziv_kategorije='Test Kategorija'
        )

        self.proizvod1 = self.Proizvod.objects.create(
            id_proizvoda='001',
            naziv_proizvoda='Test Proizvod',
            cijena_proizvoda=50,
            opis_proizvoda='Opis test proizvoda',
            proizvod_kategorija=self.kategorija1,
            proizvod_korisnik=self.korisnik1
        )

        self.narudzba1 = self.Narudzba.objects.create(
            ukupna_cijena=100,
            narudzba_korisnik=self.korisnik1
        )

        self.placanje1 = self.Placanje.objects.create(
            narudzba=self.narudzba1,
            broj_kartice='1234567890123456',
            ime_kupca='Test',
            prezime_kupca='Test',
        )

    def test_author(self):
        self.assertEquals(self.korisnik1.ime_korisnika, 'Test Ime')
        self.assertEquals(self.kategorija1.naziv_kategorije, 'Test Kategorija')
        self.assertEquals(self.proizvod1.cijena_proizvoda, 50)
        self.assertEquals(self.narudzba1.ukupna_cijena, 100)
        self.assertEquals(self.placanje1.broj_kartice, '1234567890123456')
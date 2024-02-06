from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProizvodForm(forms.ModelForm):
    class Meta:
        model = Proizvod
        fields = ['id_proizvoda', 'naziv_proizvoda', 'cijena_proizvoda', 'opis_proizvoda','slika_proizvoda', 'proizvod_kategorija']
        labels = {
			'id_proizvoda': 'ID',
			'naziv_proizvoda': 'Naziv',
			'cijena_proizvoda': 'Cijena',
			'opis_proizvoda': 'Opis',
            'slika_proizvoda': 'Slika',
			'proizvod_kategorija': 'Kategorija',		
	
		}
        widgets = {
			'id_proizvoda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}),
			'naziv_proizvoda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Naziv'}),
            'cijena_proizvoda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cijena'}),
			'opis_proizvoda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Opis'}),
            'proizvod_kategorija': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Kategorija'}),

               
		}
class ProizvodFormAdmin(forms.ModelForm):
    class Meta:
        model = Proizvod
        fields = ['id_proizvoda', 'naziv_proizvoda', 'cijena_proizvoda', 'opis_proizvoda','slika_proizvoda', 'proizvod_kategorija', 'proizvod_korisnik']
        labels = {
			'id_proizvoda': 'ID',
			'naziv_proizvoda': 'Naziv',
			'cijena_proizvoda': 'Cijena',
			'opis_proizvoda': 'Opis',
            'slika_proizvoda': 'Slika',
			'proizvod_kategorija': 'Kategorija',		
            'proizvod_korisnik' : 'Korisnik'
	
		}
        widgets = {
			'id_proizvoda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}),
			'naziv_proizvoda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Naziv'}),
            'cijena_proizvoda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cijena'}),
			'opis_proizvoda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Opis'}),
            'proizvod_korisnik': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Korisnik'}),
         
		}
class korisnikForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = ['ime_korisnika', 'prezime_korisnika', 'adresa_korisnika', 'mobitel_korisnika', 'email_korisnika']
        labels = {
			'ime_korisnika': 'Ime',
			'prezime_korisnika': 'Prezime',
			'adresa_korisnika': 'Adresa',
			'mobitel_korisnika': 'Mobitel',
			'email_korisnika': 'Email',		
	
		}
        widgets = {
			'ime_korisnika': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ime'}),
			'prezime_korisnika': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prezime'}),
            'adresa_korisnika': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresa'}),
			'mobitel_korisnika': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobitel'}),
			'email_korisnika': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),

               
		}

class RegisterUserForm(UserCreationForm):	

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'


class placanjeForm(forms.ModelForm):
    class Meta:
        model = Placanje
        fields = ['broj_kartice', 'ime_kupca', 'prezime_kupca', 'vrijeme_placanja']
        labels = {
			'broj_kartice': 'Broj kartice',
			'ime_kupca': 'Ime',
			'prezime_kupca': 'Prezime',
			
		}
        widgets = {
			'broj_kartice': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Broj karice'}),
			'ime_kupca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ime'}),
            'prezime_kupca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prezime'}),
            'vrijeme_placanja': forms.DateInput(attrs={'type': 'date'})
               
		}
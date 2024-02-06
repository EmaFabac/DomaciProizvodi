from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView, DeleteView , TemplateView, UpdateView, CreateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .form import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .cart import Cart
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


class LandingPageView(ListView):
    model = Kategorija
    template_name = 'landing.html'

    def get(self, request, *args, **kwargs):
        kate = Kategorija.objects.all()  # Assuming you want to display all categories
        return render(request, 'landing.html', {'kate': kate})


class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        results = Kategorija.objects.filter(naziv_kategorije__icontains=query)
        return render(request, 'search_results.html', {'results': results})
    
class AboutUsView(TemplateView):
    template_name = 'o_nama.html'



def detalji_kategorije(request, id_kategorije):
    kategorija = get_object_or_404(Kategorija, id_kategorije=id_kategorije)
    proizvodi = kategorija.proizvodi.all()

    return render(request, 'detalji_kategorije.html', {'kategorija': kategorija, 'proizvodi': proizvodi})

def pretrazi_proizvode(request):
    query = request.GET.get('q', '')
    proizvodi = Proizvod.objects.filter(naziv_proizvoda__icontains=query)
    return render(request, 'pretraga.html', {'query': query, 'proizvodi': proizvodi})

def login_user (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:landing')
        else:
            messages.success(request, ("Krivi unos! Pokusajte ponovo..."))	
            return redirect('main:login')
    else:
        return render(request, 'registration/login.html', {})
    

def logout_user (request):
    logout(request)
    return redirect('main:landing')

class profile (ListView):
    model = Korisnik
    template_name = 'profile.html'


def register(request):
    if request.method == 'POST':
        form1 = korisnikForm(request.POST)
        form = RegisterUserForm(request.POST)

        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.save()
            korisnik = form1.save(commit=False)
            korisnik.user = user
            korisnik.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:landing')

    else:
        form1 = korisnikForm()
        form = RegisterUserForm()

    context = {'form': form, 'form1': form1}

    return render(request, 'registration/register.html', context)


class mojiproizvodi(ListView):
    model=Proizvod
    template_name = 'mojiproizvodi.html'
class NarudzbaPopis(ListView):
    model=Narudzba
    template_name = 'mojanarudzba.html'

class ProizvodeUpdate(UpdateView):
    model = Proizvod
    form_class = ProizvodForm
    template_name = 'update_proizvod.html'
    success_url = reverse_lazy('main:mojiproizvodi')

class ProizvodeDelete(DeleteView):
    model = Proizvod
    template_name = 'delete_proizvod.html'
    success_url = reverse_lazy('main:mojiproizvodi')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = self.get_object()
        return context
    

class InfoPlacanje(ListView):
    model = Placanje
    template_name = 'placanje_info.html'
    def get_queryset(self):
        self.id_narudzbe = get_object_or_404(Placanje, narudzba=self.kwargs['narudzba'])
        return Narudzba.objects.filter(id_narudzbe=self.id_narudzbe)
    


def add_proiz(request):
    submitted = False
    if request.method == 'POST':
        if request.user.is_superuser:
            form = ProizvodFormAdmin(request.POST, request.FILES)
            if form.is_valid():
                form.save()  
                return 	redirect('main:mojiproizvodi')
        else:          
            form = ProizvodForm(request.POST,request.FILES)
            if form.is_valid():
                venue = form.save(commit=False)
                venue.proizvod_korisnik = request.user.korisnik
                venue.save()
                return 	redirect('main:mojiproizvodi')
                #form.save()
    
    else:
        if request.user.is_superuser:
            form = ProizvodFormAdmin
        else:
            form = ProizvodForm()  # This line creates a new instance of the form after saving

        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'create_proizvode.html', {'form':form, 'submitted':submitted})



def cart_summary(request):
    cart = Cart(request)
    cart_proizvod=cart.get_prods
    totals = cart.cart_total()
    return render(request, 'cart/mojenarudzbe.html', {'cart_proizvod' : cart_proizvod, 'totals' : totals})

def cart_add(request):
    cart = Cart (request)
    if request.POST.get('action')== 'post':
        id_proizvoda = int(request.POST.get('id_proizvoda'))
        proizvod = get_object_or_404(Proizvod, id=id_proizvoda)
        cart.add(proizvod=proizvod)

        cart_quantity = cart.__len__()
        response = JsonResponse({'qty: ': cart_quantity})
        messages.success(request, ("Proizvod dodan u košaricu!"))

        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
		# Get stuff
        id_proizvoda = int(request.POST.get('id_proizvoda'))
		# Call delete Function in Cart
        cart.delete(proizvod=id_proizvoda)
        response = JsonResponse({'id_proizvoda':id_proizvoda})
		#return redirect('cart_summary')
        messages.success(request, ("Proizvod izbrisan iz košarice..."))
        return response
    

def submit_order(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart_proizvod = cart.get_prods()
        totals = cart.cart_total()

        nnarudzba = Narudzba(ukupna_cijena=totals) 
        if request.user.is_authenticated:  # Check if the user is logged in
            nnarudzba.narudzba_korisnik = request.user.korisnik  

        nnarudzba.save()
        cart.clear()
        del cart.session['session_key'] 
        cart.session.modified = True
         # Save the nnarudzba object first
        nnarudzba.narudzba_proizvod.set(cart_proizvod)  # Set the many-to-many relationship after saving
        
        
        messages.success(request, "Vaša je narudžba uspješno spremljena!")
        narudzba_id = nnarudzba.id_narudzbe
        return HttpResponseRedirect(reverse_lazy('main:palcanje', kwargs={'narudzba_id': narudzba_id}))


class Placanje(CreateView):
    model = Placanje
    form_class = placanjeForm
    template_name = 'cart/placanje.html'
    

    def form_valid(self, form):
        # Get the narudzba_id from the URL
        narudzba_id = self.kwargs['narudzba_id']
        # Get the Narudzba instance
        narudzba = Narudzba.objects.get(id_narudzbe=narudzba_id)
        # Assign the Narudzba instance to the Placanje model
        self.object = form.save(commit=False)
        self.object.narudzba = narudzba
        self.object.save()
        return super().form_valid(form)
    success_url = reverse_lazy('main:landing')
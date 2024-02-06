from django.urls import path
from . import views
from.views import SearchResultsView , AboutUsView

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('o_nama/', AboutUsView.as_view(), name='about_us'),
    path('kategorija/<int:id_kategorije>/', views.detalji_kategorije, name='detalji_kategorije'),
    path('pretraga/', views.pretrazi_proizvode, name='pretrazi_proizvode'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('mojiproizvodi/', views.mojiproizvodi.as_view(), name='mojiproizvodi'),
    path('mojiproizvodi/update/<int:pk>', views.ProizvodeUpdate.as_view(), name='update'),
    path('mojiproizvodi/delete/<int:pk>', views.ProizvodeDelete.as_view(), name='delete'),
    path('mojiproizvodi/add/', views.add_proiz, name='add'),
    path('cart/', views.cart_summary, name = 'cart_summary' ),
    path('cart/add/', views.cart_add, name = 'cart_add' ),
    path('cart/delete/', views.cart_delete, name = 'cart_delete' ),
    path('cart/naruci/', views.submit_order, name = 'sumbite_order' ),
    path('narudzba/', views.NarudzbaPopis.as_view(), name='popis'),
    path('cart/placanje/<int:narudzba_id>/', views.Placanje.as_view(), name='palcanje'),
    path('narudzba/<int:narudzba_id>/info', views.InfoPlacanje.as_view(), name='placanje_info')
]
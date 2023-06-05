from django.urls import path
from . import views

urlpatterns = [
    path('produits/', views.produits_list, name='produits_list'),
    path('produits/<int:produit_id>/', views.produit_detail, name='produit_detail'),
    path('panier/', views.panier, name='panier'),
    path('passer_commande/', views.passer_commande, name='passer_commande'),
    path('commande_confirmee/', views.commande_confirmee, name='commande_confirmee'),
]

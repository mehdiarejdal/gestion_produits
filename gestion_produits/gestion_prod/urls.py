from django.urls import path
# from .views import produits, commandes
from . import views
urlpatterns = [
    # path('api/produits/', produits, name='produits'),
    # path('api/commandes/', commandes, name='commandes'),
    path('produits/', views.produits_list, name='produits_list'),
    path('produits/<int:produit_id>/', views.produit_detail, name='produit_detail'),
    path('panier/', views.panier, name='panier'),
    path('passer_commande/', views.passer_commande, name='passer_commande'),
]

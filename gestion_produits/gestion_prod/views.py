from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produit, Commande
from .api.serializers import ProduitSerializer, CommandeSerializer




@api_view(['GET', 'POST'])
def produits(request):
    if request.method == 'GET':
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def commandes(request):
    if request.method == 'GET':
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def produits_list(request):
    produits = Produit.objects.all()
    return render(request, 'gestion_prod/produits_list.html', {'produits': produits})


@api_view(['GET'])
def produit_detail(request, produit_id):
    try:
        produit = Produit.objects.get(id=produit_id)
    except Produit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return render(request, 'gestion_prod/produit_detail.html', {'produit': produit})


@api_view(['GET'])
def panier(request):
    # Logic to retrieve and display the items in the shopping cart
    return render(request, 'gestion_prod/panier.html')


@api_view(['POST'])
def passer_commande(request):
    # Logic to process the order and save it in the database
    return Response(status=status.HTTP_201_CREATED)

def afficher_produits(request):
    produits = Produit.objects.all()
    return render(request, 'gestion_prod/produits.html', {'produits': produits})

def afficher_panier(request):
    return render(request, 'gestion_prod/panier.html')

def passer_commande(request):
    if request.method == 'POST':
        serializer = CommandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'gestion_prod/commande_confirmee.html')
    return render(request, 'gestion_prod/passer_commande.html')

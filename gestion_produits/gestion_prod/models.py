from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Commande(models.Model):
    date = models.DateField()
    produits = models.ManyToManyField(Produit, through='LigneCommande')

class LigneCommande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    quantite = models.IntegerField()


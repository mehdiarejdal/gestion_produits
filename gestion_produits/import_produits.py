import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_produits.settings')

# Initialize Django
django.setup()

import json
from gestion_prod.models import Produit

# Path to your produits.json file
json_file_path = 'gestion_prod/static/json/produits.json'

def import_products():
    with open(json_file_path) as file:
        products = json.load(file)
        for product_data in products:
            produit = Produit(
                nom=product_data['nom'],
                prix=product_data['prix'],
                description=product_data['description']
            )
            produit.save()


if __name__ == '__main__':
    import_products()

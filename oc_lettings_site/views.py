"""
Vues de l'application pour afficher la page d'accueil

Ce fichier contient les vues qui rendent les pages principales de l'application. Actuellement,
il inclut une vue pour la page d'accueil
"""
from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Affiche la page d'accueil de l'application

    Cette fonction rend la page HTML 'index.html' lorsque l'utilisateur accède à la page d'accueil

    Paramètres :
        request (HttpRequest) : Objet de requête HTTP

    Retour :
        HttpResponse : Page d'accueil rendue avec le template 'index.html'
    """
    return render(request, 'index.html')

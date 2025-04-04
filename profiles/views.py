"""
Vues pour l'application 'profiles'.

Ce fichier contient les vues permettant d'afficher la liste des profils et
les détails d'un profil spécifique pour l'application 'profiles'. Il inclut
deux vues principales : une pour l'index des profils et une pour afficher
les informations d'un profil individuel.
"""
from django.shortcuts import render
import logging
from .models import Profile

logger = logging.getLogger("profiles")

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """
    Affiche la liste des profils.

    Cette vue récupère tous les profils enregistrés dans la base de données
    et les passe au template 'profiles/index.html'. Elle permet de visualiser
    une liste de tous les utilisateurs ayant un profil associé.

    Paramètres :
        request (HttpRequest) : L'objet de requête HTTP.

    Retour :
        HttpResponse : La réponse contenant le rendu du template avec la liste
        des profils.
    """
    try:
        profiles_list = Profile.objects.all()
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des données : {e}")
        raise
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor
# id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Affiche les détails d'un profil utilisateur spécifique.

    Cette vue récupère un profil spécifique en fonction du nom d'utilisateur
    et le passe au template 'profiles/profile.html'. Elle permet de visualiser
    des informations détaillées sur un utilisateur, telles que la ville favorite.

    Paramètres :
        request (HttpRequest) : L'objet de requête HTTP.
        username (str) : Le nom d'utilisateur dont le profil doit être affiché.

    Retour :
        HttpResponse : La réponse contenant le rendu du template avec les
        informations du profil de l'utilisateur.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning(f"Profil introuvable pour : {username}")
        raise
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des données : {e}")
        raise
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

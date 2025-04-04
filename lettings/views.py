"""
Vues de l'application Lettings

Ce fichier contient les vues permettant d'afficher la liste des locations et les détails
d'une location spécifique
"""
from django.shortcuts import render
import logging
from .models import Letting

logger = logging.getLogger("lettings")


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum ante ipsum primis in
# faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Affiche la liste des locations disponibles

    Récupère toutes les locations enregistrées et les passe au template 'lettings/index.html'

    Paramètres :
        request (HttpRequest) : Objet de requête HTTP

    Retour :
        HttpResponse : Page HTML affichant la liste des locations
    """
    try:
        lettings_list = Letting.objects.all()
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des données : {e}")
        raise
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae
# efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est
# ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse
# potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis
# ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris condimentum
# auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue
# pulvinar sit amet.
def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique

    Récupère une location à partir de son identifiant et affiche ses informations dans le template
    'lettings/letting.html'

    Paramètres :
        request (HttpRequest) : Objet de requête HTTP
        letting_id (int) : Identifiant unique de la location

    Retour :
        HttpResponse : Page HTML affichant les détails de la location
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning(f"ID introuvable : {letting_id}")
        raise
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des données : {e}")
        raise
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

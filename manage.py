"""
Script de gestion de Django.

Ce script est utilisé pour lancer les commandes de gestion Django via la ligne de commande.
Il définit l'environnement Django en fonction du fichier de paramètres approprié et
exécute les commandes via `execute_from_command_line` de Django.
"""
import os
import sys
import logging

logger = logging.getLogger('django')

def main():
    """
    Exécute la commande de gestion de Django.

    Cette fonction configure l'environnement Django en définissant le module de
    paramètres à utiliser et en appelant la fonction `execute_from_command_line`
    pour traiter les arguments de la ligne de commande.

    Elle est utilisée pour exécuter les commandes comme `python manage.py migrate`,
    `python manage.py runserver`, etc.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logger.error(f"Erreur d'importation de Django : {exc}")
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

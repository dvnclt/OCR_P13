"""
Middleware pour journaliser les erreurs non gérées à l'aide du module logging.

Capture les exceptions levées durant le traitement des requêtes et les
enregistre sans interrompre la gestion normale des erreurs par Django.
"""
import logging


logger = logging.getLogger(__name__)


class ErrorLoggingMiddleware:
    """
    Middleware pour capturer et logger les erreurs non gérées.
    """
    def __init__(self, get_response):
        """
        Initialise le middleware avec la fonction qui traite la requête
        suivante
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Intercepte la requête, traite la réponse, et capture les erreurs non
        gérées
        """
        try:
            response = self.get_response(request)
        except Exception as e:
            logger.error(f"Erreur non gérée : {e}", exc_info=True)
            raise
        return response

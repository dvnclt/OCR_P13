### Configuration de Sentry
1. Installez `sentry-sdk` :

```bash
pip install sentry-sdk
```

2. Ajoutez votre DSN Sentry dans vos variables d'environnement :
```bash
SENTRY_DSN=https://<your_sentry_dsn>
```

3. La configuration de Sentry se trouve dans `settings.py` :
```bash
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
)
```

4. La configuration du logging se trouve dans `settings.py` :
```bash
LOGGING = {
    ...
}
```

### Test de Sentry
Des vues et urls de test ont été définies dans l'app `oc_lettings_site`.

`def test_sentry_error` : Provoque une erreur (division par zéro) pour vérifier que Sentry la capture bien.
Le test se fait depuis l'URL : `http://127.0.0.1:8000/sentry-test/`

`def test_middleware_error` : Provoque une erreur non gérée pour vérifier que Sentry la capture bien.
Le test se fait depuis l'URL : `http://127.0.0.1:8000/middleware-test/`
# Documentation Technique

## 1. Description du projet

Ce projet est une application Django appelée **Holiday Homes**, qui permet de gérer des profils et des locations de vacances. Elle inclut des fonctionnalités comme :

- Gestion des profils utilisateurs.
- Gestion des annonces de locations.
- Administration via l'interface Django Admin.
- Intégration de Sentry pour la gestion des erreurs.
- L'application est conteneurisée avec Docker et déployée sur Render via un pipeline CI/CD.

## 2. Instructions d'installation

### Prérequis

- Python 3.9 ou supérieur.
- Docker et Docker Compose.
- Un compte Docker Hub.
- Un compte Render.

### Étapes d'installation

1. Clonez le dépôt Git :

    ```bash
    git clone <url-du-dépôt>
    ```

2. Créez l'environnement virtuel et installez les dépendances Python :

    ```bash
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. Configurez les variables d'environnement dans un fichier `.env` :

    Créez un fichier `.env` à la racine du projet et ajoutez les variables suivantes :

    ```
    SENTRY_DSN=<votre-dsn-sentry>
    DOCKER_USERNAME=<votre-nom-utilisateur-docker>
    ```

4. Lancez le serveur local :

    ```bash
    ./run_docker.sh
    ```
    
    Accédez à l'application à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000).


## 3. Technologies et langages utilisés

- Langage principal : Python 3.9.
- Framework : Django 3.0.
- Base de données : SQLite (en développement) et PostgreSQL (en production - Render).
- Conteneurisation : Docker.
- CI/CD : GitHub Actions.
- Hébergement : Render.
- Gestion des erreurs : Sentry.

## 4. Structure de la base de données et des modèles

### Modèles principaux

#### **Profile** (dans l'application `profiles`) :
- `user` : Clé étrangère vers le modèle utilisateur de Django (`django.contrib.auth.models.User`).
- `favorite_city` : Ville préférée de l'utilisateur (type `CharField`).

#### **Address** (dans l'application `lettings`) :
- `number` : Numéro de rue (type `PositiveIntegerField`, max : 9999).
- `street` : Nom de la rue (type `CharField`, max : 64 caractères).
- `city` : Ville (type `CharField`, max : 64 caractères).
- `state` : Code d'état (type `CharField`, exactement 2 caractères).
- `zip_code` : Code postal (type `PositiveIntegerField`, max : 99999).
- `country_iso_code` : Code ISO du pays (type `CharField`, exactement 3 caractères).

#### **Letting** (dans l'application `lettings`) :
- `title` : Titre de la location (type `CharField`, max : 256 caractères).
- `address` : Adresse associée à la location (relation `OneToOneField` avec le modèle `Address`).

### Exemple de structure des tables dans la base de données

#### **Table `profiles_profile` :**

| Champ        | Type            | Description                               |
|--------------|-----------------|-------------------------------------------|
| `id`         | `AutoField`     | Identifiant unique du profil.             |
| `user_id`    | `ForeignKey`    | Référence à un utilisateur Django.       |
| `favorite_city` | `CharField`   | Ville préférée de l'utilisateur.         |

#### **Table `lettings_address` :**

| Champ            | Type                 | Description                                         |
|------------------|----------------------|-----------------------------------------------------|
| `id`             | `AutoField`          | Identifiant unique de l'adresse.                    |
| `number`         | `PositiveIntegerField`| Numéro de rue (max : 9999).                         |
| `street`         | `CharField`          | Nom de la rue (max : 64 caractères).                |
| `city`           | `CharField`          | Ville (max : 64 caractères).                        |
| `state`          | `CharField`          | Code d'état (exactement 2 caractères).              |
| `zip_code`       | `PositiveIntegerField`| Code postal (max : 99999).                         |
| `country_iso_code` | `CharField`        | Code ISO du pays (exactement 3 caractères).         |

#### **Table `lettings_letting` :**

| Champ        | Type               | Description                                        |
|--------------|--------------------|----------------------------------------------------|
| `id`         | `AutoField`        | Identifiant unique de la location.                 |
| `title`      | `CharField`        | Titre de la location (max : 256 caractères).       |
| `address_id` | `OneToOneField`    | Référence à une adresse unique.                    |

### Relations entre les modèles
- **Profile** est lié à un utilisateur Django via une clé étrangère (`ForeignKey`).
- **Letting** est lié à une **Address** via une relation `OneToOneField` (une location a une adresse unique).


## 5. Interfaces de programmation

| Nom                            | URL                                | Méthode | Description                                                 |
|---------------------------------|------------------------------------|---------|-------------------------------------------------------------|
| **Page d'accueil**              | `/`                                | `GET`   | Affiche la page d'accueil de l'application.                 |
| **Liste des locations**         | `lettings`                         | `GET`   | Affiche la liste des locations disponibles.                 |
| **Détail d'une location**       | `/lettings/<int:letting_id>/`      | `GET`   | Affiche les détails d'une location spécifique.              |
| **Liste des profils**           | `profiles`                         | `GET`   | Affiche la liste des profils utilisateurs.                  |
| **Détail d'un profil utilisateur** | `/profiles/<str:username>/`      | `GET`   | Affiche les détails d'un profil utilisateur spécifique.     |
| **Administration Django**       | `/admin/`                          | `GET`   | Permet d'accéder à l'interface d'administration Django.     |
| **Test Sentry**                 | `/sentry-test/`                    | `GET`   | Provoque une erreur pour tester l'intégration avec Sentry.  |
| **Test Middleware**             | `/middleware-test/`                | `GET`   | Provoque une erreur non gérée pour tester le middleware.    |


## 6. Guide d'utilisation

### Cas d'utilisation

#### 1. Gérer les profils utilisateurs
La gestion des profils utilisateurs (création, modification, suppression) se fait via le panneau d'administration Django.

**Étapes :**
1. Accédez à `/admin/` et connectez-vous avec vos identifiants administrateur.
2. Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`
3. Dans la section **Profiles**, cliquez sur **Add** pour créer un nouveau profil ou sélectionnez un profil existant pour le modifier.
4. Remplissez les informations nécessaires et enregistrez.

#### 2. Ajouter une annonce de location
L'ajout et la gestion des annonces de locations se font également via le panneau d'administration Django.

**Étapes :**
1. Accédez à `/admin/` et connectez-vous avec vos identifiants administrateur.
2. Dans la section **Lettings**, cliquez sur **Add** pour créer une nouvelle annonce ou sélectionnez une annonce existante pour la modifier.
3. Remplissez les informations nécessaires et enregistrez.

## 7. Procédures de déploiement et de gestion

### Déploiement

#### Récapitulatif du fonctionnement du déploiement
Le déploiement utilise un pipeline CI/CD configuré dans le fichier `.github/workflows/ci.yml`. Ce pipeline :
1. Exécute des tests et vérifie la qualité du code.
2. Construit une image Docker de l'application.
3. Pousse automatiquement l'image Docker sur Docker Hub.
4. Déclenche un déploiement sur Render en utilisant un **Deploy Hook**.

#### Configuration requise
1. **Docker Hub** :
   - Un compte Docker Hub est nécessaire pour stocker l'image Docker.
   - Générez un Token pour permettre à Render d'accéder à l'image.
   - Les secrets `DOCKER_USERNAME` et `DOCKER_TOKEN` doivent être configurés dans les **Secrets GitHub**.

2. **Render** :
   - Un compte Render est requis.
   - Configurez un service Docker (Existing Image) sur Render pour déployer l'application.
   - Servez-vous du Token généré précédemment sur Docker pour l'authentification.
   - Ajoutez un **Deploy Hook** dans Render et configurez-le comme secret `RENDER_DEPLOY_HOOK_URL` dans GitHub.

3. **Variables d'environnement** :
   - Les variables suivantes doivent être définies dans l'environnement Render :
     - `SECRET_KEY`: Une clé secrète pour Django.
     - `SENTRY_DSN`: Le DSN pour Sentry (facultatif, pour la gestion des erreurs).

#### Étapes pour effectuer le déploiement
1. **Poussez vos modifications sur GitHub** :
   - Assurez-vous que vos modifications sont poussées sur la branche `main` ou `dev` (selon votre configuration).

   - A titre informatif, voilà les différentes configurations en fonction de la branche.

    | Action GitHub       | CI/CD exécuté ? | Déploiement effectué ? |
    | ------------------- | --------------- | ---------------------- |
    | Push sur main        | ✅ Oui          | ✅ Oui                 |
    | Merge vers main      | ✅ Oui          | ✅ Oui                 |
    | Push sur dev         | ✅ Oui          | ❌ Non                 |
    | Merge vers dev       | ✅ Oui          | ❌ Non                 |


2. **Pipeline CI/CD** :
   - Une fois les modifications poussées, le pipeline CI/CD s'exécute automatiquement :
     - Les tests sont exécutés.
     - Une image Docker est construite et poussée sur Docker Hub.
     - Un déploiement est déclenché sur Render via le **Deploy Hook**.

3. **Vérifiez le déploiement** :
   - Une fois le pipeline terminé, accédez à l'URL fournie par Render (par exemple, `https://holiday-homes-1gb4.onrender.com`) pour vérifier que l'application fonctionne correctement.

#### Notes supplémentaires
- Si des modifications sont apportées au code, poussez-les simplement sur GitHub pour déclencher un nouveau déploiement.
- Consultez les logs GitHub Actions pour vérifier l'état du pipeline CI/CD.
- Consultez les logs Render en cas de problème pour identifier les erreurs.
- Ne pas oublier de passer `DEBUG = False` dans `settings.py` pour une mise en production
- Ne pas oublier de configurer `ALLOWED_HOSTS` dans `settings.py`

## 8. Journalisation
### Configuration de Sentry
Si non installé depuis le `requirements.txt` :
1. Installez `sentry-sdk` :

```bash
pip install sentry-sdk
```

2. Ajoutez votre DSN Sentry dans `.env` :
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


import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str():
    """
    Teste la méthode __str__ du modèle Profile.
    """
    user = User.objects.create_user(username="testuser", password="password123")
    profile = Profile.objects.create(user=user, favorite_city="Paris")
    assert str(profile) == "testuser"


@pytest.mark.django_db
def test_profile_favorite_city():
    """
    Teste que le champ favorite_city est correctement enregistré.
    """
    user = User.objects.create_user(username="testuser", password="password123")
    profile = Profile.objects.create(user=user, favorite_city="Paris")
    assert profile.favorite_city == "Paris"


@pytest.mark.django_db
def test_profile_user_relationship():
    """
    Teste la relation OneToOne entre Profile et User.
    """
    user = User.objects.create_user(username="testuser", password="password123")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    # Vérifie que le profil est lié à l'utilisateur
    assert profile.user == user

    # Vérifie que l'utilisateur a un profil
    assert user.profile == profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    """
    Teste la vue index de profiles pour s'assurer qu'elle retourne un code 200
    et utilise le bon template.
    """
    # Création de données fictives
    user1 = User.objects.create_user(username="user1", password="password123")
    user2 = User.objects.create_user(username="user2", password="password123")
    Profile.objects.create(user=user1, favorite_city="Paris")
    Profile.objects.create(user=user2, favorite_city="London")

    # Requête vers la vue
    response = client.get(reverse('profiles_index'))

    # Assertions
    assert response.status_code == 200
    assert 'profiles/index.html' in [t.name for t in response.templates]
    assert b"user1" in response.content
    assert b"user2" in response.content


@pytest.mark.django_db
def test_profile_view(client):
    """
    Teste la vue profile pour s'assurer qu'elle retourne un code 200,
    utilise le bon template et affiche les informations correctes.
    """
    # Création de données fictives
    user = User.objects.create_user(username="testuser", password="password123")
    profile = Profile.objects.create(user=user, favorite_city="Tokyo")  # noqa: F841

    # Requête vers la vue
    response = client.get(reverse('profile', kwargs={'username': user.username}))

    # Assertions
    assert response.status_code == 200
    assert 'profiles/profile.html' in [t.name for t in response.templates]
    assert b"testuser" in response.content
    assert b"Tokyo" in response.content

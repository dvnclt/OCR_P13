import pytest
from django.test import Client
from django.urls import reverse


client = Client()


def test_dummy():
    assert 1


def test_index_view():
    """
    Teste la vue index pour s'assurer qu'elle retourne un code 200
    et utilise le bon template.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_index_url():
    """
    Teste l'URL de la page d'accueil.
    """
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_lettings_index_url():
    """
    Teste l'URL de la page des lettings.
    """
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_index_url():
    """
    Teste l'URL de la page des profiles.
    """
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200

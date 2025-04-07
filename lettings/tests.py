import pytest
from django.urls import reverse

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_address_str():
    """
    Teste la méthode __str__ du modèle Address.
    """
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Springfield",
        state="SP",
        zip_code=12345,
        country_iso_code="USA"
    )
    assert str(address) == "123 Main Street"


@pytest.mark.django_db
def test_letting_str():
    """
    Teste la méthode __str__ du modèle Letting.
    """
    address = Address.objects.create(
        number=456,
        street="Elm Street",
        city="Shelbyville",
        state="SH",
        zip_code=67890,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    assert str(letting) == "Test Letting"


@pytest.mark.django_db
def test_letting_address_relationship():
    """
    Teste la relation OneToOne entre Letting et Address.
    """
    address = Address.objects.create(
        number=789,
        street="Oak Street",
        city="Capital City",
        state="CC",
        zip_code=54321,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Unique Letting", address=address)

    # Vérifie que l'adresse associée est correcte
    assert letting.address == address

    # Vérifie que l'adresse est accessible via la relation inverse
    assert address.letting == letting


@pytest.mark.django_db
def test_lettings_index_view(client):
    """
    Teste la vue index de lettings pour s'assurer qu'elle retourne un code 200
    et utilise le bon template.
    """
    # Création de données fictives
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Springfield",
        state="SP",
        zip_code=12345,
        country_iso_code="USA"
    )
    Letting.objects.create(title="Test Letting", address=address)

    # Requête vers la vue
    response = client.get(reverse('lettings_index'))

    # Assertions
    assert response.status_code == 200
    assert 'lettings/index.html' in [t.name for t in response.templates]
    assert b"Test Letting" in response.content


@pytest.mark.django_db
def test_letting_view(client):
    """
    Teste la vue letting pour s'assurer qu'elle retourne un code 200,
    utilise le bon template et affiche les détails corrects.
    """
    # Création de données fictives
    address = Address.objects.create(
        number=456,
        street="Elm Street",
        city="Shelbyville",
        state="SH",
        zip_code=67890,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Another Letting", address=address)

    # Requête vers la vue
    response = client.get(reverse('letting',
                                  kwargs={'letting_id': letting.id}))

    # Assertions
    assert response.status_code == 200
    assert 'lettings/letting.html' in [t.name for t in response.templates]
    assert b"Another Letting" in response.content
    assert b"456 Elm Street" in response.content

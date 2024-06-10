import pytest
from django.test import Client
from django.urls import reverse, resolve
from .models import Address, Letting
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def address():
    address = Address.objects.create(
        number="25",
        street="avenue du parc",
        city="Paris",
        state="France",
        zip_code="75002",
        country_iso_code="FR"
    )
    return address


@pytest.fixture
def letting(address):
    letting = Letting.objects.create(
        title="test",
        address=address
    )
    return letting


def test_letting_index_url():
    path = reverse('lettings_index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"


@pytest.mark.django_db
def test_letting_id_url(letting):
    assert hasattr(letting, 'id')  # Ensure that the 'letting' object has an 'id' attribute.
    path = reverse('letting', kwargs={'letting_id': letting.id})
    assert path == f"/lettings/{letting.id}/"
    assert resolve(path).view_name == "letting"


@pytest.mark.django_db
def test_model_adress(address):
    expected_value = "25 avenue du parc"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_model_letting(letting):
    expected_value = "test"
    assert str(letting) == expected_value


@pytest.mark.django_db
def test_letting_id_view(letting):
    client = Client()
    path = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()
    assert "<title>test</title>" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_letting_index_view():
    client = Client()
    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()
    assert "<title>Lettings</title>" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")

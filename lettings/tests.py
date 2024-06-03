from django.test import Client
import pytest

from .models import Address, Letting

client = Client()

@pytest.fixture
def letting_with_address():
    address = Address.objects.create(
        number="1",
        street="20 avenue du parc",
        city="Paris",
        state="75",
        zip_code="75002",
        country_iso_code="FR"
    )
    letting = Letting.objects.create(
        title="test",
        address=address
    )
    return letting

@pytest.mark.django_db
def test_index_response(client):
    response = client.get("/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_lettings_list_response(client):
    response = client.get("/lettings/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_something(letting_with_address):
    response = client.get(f"/lettings/1/")
    assert response.status_code == 200
    # Dans ce test, letting_with_address contiendra l'objet Letting créé par la fixture
    assert letting_with_address.title == "test"
    assert letting_with_address.address.city == "Paris"

# @pytest.mark.django_db
# def test_letting_detail_response(client):
#     address = Address.objects.create(
#         number="1",
#         street="20 avenue du parc",
#         city="Paris",
#         state="75",
#         zip_code="75002",
#         country_iso_code="FR"
#     )
#     letting =   Letting.objects.create(
#         title="test",
#         address=address
#     )
#     response = client.get(f"/lettings/1/")
#     assert response.status_code == 200
#     assert b"Paris" in response.content

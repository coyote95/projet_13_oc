import pytest
from django.test import Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed


def test_dummy():
    assert 1


def test_index_url():
    path = reverse('index')
    assert path == f"/"
    assert resolve(path).view_name == "index"


@pytest.mark.django_db
def test_admin_url():
    path = reverse('admin:index')
    assert path == "/admin/"
    assert resolve(path).url_name.split(":")[-1] == "index"


@pytest.mark.django_db
def test_index_view():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()
    assert "<title>Holiday Homes</title>" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


@pytest.mark.django_db
def test_wrong_url():
    client = Client()
    response = client.get("/toto/")
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_integration():
    client = Client()
    home_url = reverse('index')
    response = client.get(home_url)
    assert response.status_code == 200
    profiles_url = reverse('profiles_index')
    response = client.get(profiles_url)
    assert response.status_code == 200
    letting_url = reverse('lettings_index')
    response = client.get(letting_url)
    assert response.status_code == 200

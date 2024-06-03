import pytest
from django.test import Client
from django.urls import reverse, resolve
from .models import Profile
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User


@pytest.fixture
def profile():
    user = User.objects.create_user(username="julien", first_name="Julien", last_name="Dupont")
    profile = Profile.objects.create(
        user=user,
        favorite_city="avenue du parc",
    )
    return profile


def test_profile_index_url():
    path = reverse('profiles_index')
    assert path == f"/profiles/"
    assert resolve(path).view_name == "profiles_index"


@pytest.mark.django_db
def test_profile_username_url(profile):
    path = reverse('profile', kwargs={'username': profile.user.username})
    assert path == f"/profiles/{profile.user.username}/"
    assert resolve(path).view_name == "profile"


@pytest.mark.django_db
def test_model_profile(profile):
    expected_value = "julien"
    assert str(profile) == expected_value


@pytest.mark.django_db
def test_profile_username_view(profile):
    client = Client()
    path = reverse('profile', kwargs={'username': profile.user.username})
    response = client.get(path)
    content = response.content.decode()
    assert "<title>julien</title>" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profile_index_view():
    client = Client()
    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()
    assert "<title>Profiles</title>" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")

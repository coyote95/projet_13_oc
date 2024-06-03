"""
This module defines URL patterns for the 'profiles' application.

Routes:
    - "" (profiles_index): The index page of the profiles application.
    - "<str:username>/": The detail page for a specific profile, identified by its username.

"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<str:username>/", views.profile, name="profile"),
]

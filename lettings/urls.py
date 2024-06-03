"""
This module defines URL patterns for the 'lettings' application.

Routes:
    - "" (lettings_index): The index page of the lettings application.
    - "<int:letting_id>/": The detail page for a specific letting, identified by its ID.
"""


from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]

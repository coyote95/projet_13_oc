"""
This module defines URL patterns for the oc_lettings_site project.

Routes:
    - "" (index): The index page of the site.
    - "lettings/": Routes for the lettings application.
    - "profiles/": Routes for the profiles application.
    - "admin/": The Django admin interface.

Error Handlers:
    - handler404: Custom handler for 404 errors.
    - handler500: Custom handler for 500 errors.
"""

from django.contrib import admin
from django.urls import path, include
from .views import custom_404, custom_500

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]

handler404 = custom_404
handler500 = custom_500

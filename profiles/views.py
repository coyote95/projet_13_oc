"""
This module defines views for rendering templates in the 'profiles' application.

Functions:
    index
    profile
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile

import logging

logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
      Renders the profiles/index.html template, displaying a list of profiles.

      Parameters:
          request (HttpRequest): The HTTP request object.

      Returns:
          HttpResponse: The HTTP response containing the rendered template.
      """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,it.
# Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Renders the profiles/profile.html template, displaying details of a specific profile.

    Parameters:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The HTTP response containing the rendered template.
    """

    profile = get_object_or_404(Profile, user__username=username)
    logger.info(f"Accessing profile details for username: {username}, Profile ID: {profile.id}")
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)

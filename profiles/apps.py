"""
This module defines the configuration for the 'profiles' application in a Django project.

Classes:
    ProfilesConfig
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the 'profiles' application.

    Attributes:
        name (str): The name of the Django application. It should match the name
                    of the application module.
    """
    name = "profiles"

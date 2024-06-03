"""
This module defines the configuration for the 'oc_lettings_site' application in a Django project.

Classes:
    OCLettingsSiteConfig
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Configuration class for the 'oc_lettings_site' application.

    Attributes:
        name (str): The name of the Django application. It should match the name
                    of the application module.
    """
    name = "oc_lettings_site"

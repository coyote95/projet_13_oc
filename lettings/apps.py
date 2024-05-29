"""
This module defines the configuration for the 'lettings' application in a Django project.

Classes:
    LettingsConfig
"""

from django.apps import AppConfig

class LettingsConfig(AppConfig):
    """
    Configuration class for the 'lettings' application.

       Attributes:
           name (str): The name of the Django application. It should match the name
                        of the application module.
       """
    name = "lettings"

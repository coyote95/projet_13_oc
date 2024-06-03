"""
This module defines the models for the 'profiles' application in a Django project.

Classes:
    Profile
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class to represent a user profile.

    Attributes:
        user (OneToOneField): A one-to-one relationship to the User model.
        favorite_city (CharField): The user's favorite city, can be left blank.

    Methods:
        __str__(): Returns the username associated with the profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
            Returns a string representation of the profile.

            Returns:
                (str): The username of the user associated with the profile.
            """
        return self.user.username

    class Meta:
        """
              Meta class for Profile model.

              Attributes:
                  db_table (str): The name of the database table for the model.
              """
        db_table = "oc_lettings_site_profile"

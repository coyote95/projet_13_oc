"""
This module defines the models for the 'lettings' application in a Django project.

Classes:
    Address
    Letting
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
       A class to represent an address.

       Attributes:
            number (PositiveIntegerField): The street number of the address.
            street (CharField): The street name of the address.
            city (CharField): The city of the address.
            state (CharField): The state abbreviation of the address (2 characters).
            zip_code (PositiveIntegerField): The zip code of the address.
            country_iso_code (CharField): The ISO country code of the address (3 characters).


       Methods:
           __str__(): Print the representation of the address.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
            Returns a string representation of the address.

            Returns:
                (str):A string in the format 'number street'.
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
             Meta class for Address model.

             Attributes:
                db_table (str): The name of the database table for the model.
                verbose_name_plural (str): The plural name to use for the model in the Django admin interface.
         """
        db_table = "oc_lettings_site_address"
        verbose_name_plural = "Adresses"


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
            Returns a string representation of the letting.
                Returns:
                    (str):   The title of the letting.
        """
        return self.title

    class Meta:
        """
            Meta class for Letting model.

            Attributes:
                db_table (str): The name of the database table for the model.
        """
        db_table = "oc_lettings_site_letting"

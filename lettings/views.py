"""
This module defines views for the 'lettings' application.

Functions:
    index
    letting
"""

from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging

logger = logging.getLogger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Renders the index.html template, displaying a list of all lettings.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered template.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium,
# purus urna vulputate arcu, vitae efficitur lacus justo nec purus.
# Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit libero
# in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis
# ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
     Renders the letting.html template, displaying details of a specific letting.

     Parameters:
         request (HttpRequest): The HTTP request object.
         letting_id (int): The ID of the letting to display.

     Returns:
         HttpResponse: The HTTP response containing the rendered template.
     """
    letting = get_object_or_404(Letting, id=letting_id)
    logger.info(f"Accessing details of letting with ID: {letting_id}, Title: {letting.title}, "
                f" Address: {letting.address}")

    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)

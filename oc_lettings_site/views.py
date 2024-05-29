"""
This module defines views for rendering templates in the 'lettings' application.

Functions:
    index
    custom_404
    custom_500
"""

from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros,vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque
# iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
        Renders the index.html template.

        Returns:
            HttpResponse: The HTTP response containing the rendered template.
      """
    return render(request, "index.html")

def custom_404(request, exception):
    """
    Renders the 404.html template for page not found errors.

    Parameters:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The HTTP response containing the rendered template.
    """
    return render(request, '404.html', status=404)

def custom_500(request):
    """
    Renders the 500.html template for server errors.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered template.
    """

    return render(request, '500.html', status=500)

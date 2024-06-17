.. Orange County Lettings documentation master file, created by
   sphinx-quickstart on Mon Jun 17 12:04:30 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Orange County Lettings's documentation!
==================================================

Project Description
----------------------

Modifying a Django application for Orange County Lettings, a startup in the real estate rental sector.

Installation
------------

To install and run this project locally, follow these steps:

1. Clone the repository from GitHub:

   .. code-block:: bash

      git clone https://github.com/coyote95/projet_13_oc.git
      cd projet_13_oc

2. Create and activate a virtual environment on Windows:

   .. code-block:: bash

      python -m venv ENV
      source ENV\Scripts\activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt
4. Run Django migrations:

   .. code-block:: bash

      python manage.py migrate

5. Collect static files:

   .. code-block:: bash

      python manage.py collectstatic

6. Start the Django development server:

   .. code-block:: bash

      python manage.py runserver

7. Navigate to http://localhost:8000 in your browser to view the application.



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

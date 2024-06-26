Welcome to Orange County Lettings's documentation!
==================================================

Contents
--------

.. contents::
   :depth: 2

Project Description
-------------------

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

Quick start
-----------

The site uses a basic modular architecture of Django with a configuration directory named oc_lettings_site and two application directories named lettings to manage properties and profiles to manage users. There is also a static directory handling elements such as images, CSS files, JavaScript files, fonts, and other similar resources. Additionally, there is a templates directory containing basic error pages and the main index page of the website.

Technologies Used
-----------------

- Framework: Django
- Database: sqlite3
- Languages: Python, HTML/CSS
- Containerization: Docker
- CI/CD: GitHub Actions
- Hosting: Render

Database Structure
------------------

The project uses sqlite3 as the main database. Here are the primary data models:

.. image:: _static/diagram.png
   :alt: ER diagram
   :width: 600px
   :align: center

Programming Interfaces
----------------------

1. **URL Configurations**

   - `oc_lettings_site/urls.py`:

     .. code-block:: python

        urlpatterns = [
            path("", views.index, name="index"),
            path("lettings/", include("lettings.urls")),
            path("profiles/", include("profiles.urls")),
            path("admin/", admin.site.urls),
        ]

   - `lettings/urls.py`:

     .. code-block:: python

        urlpatterns = [
            path("", views.index, name="lettings_index"),
            path("<int:letting_id>/", views.letting, name="letting"),
        ]

   - `profiles/urls.py`:

     .. code-block:: python

        urlpatterns = [
            path("", views.index, name="profiles_index"),
            path("<str:username>/", views.profile, name="profile"),
        ]

2. **Views**

   - `oc_lettings_site/views.py`:

     .. code-block:: python

         def index(request):
             logger.info("Rendering index.html")
             return render(request, "index.html")

         def custom_404(request, exception):
             logger.error(f"Page not found: {request.path}")
             return render(request, '404.html', status=404)

         def custom_500(request):
             logger.error("Internal server error")
             return render(request, "500.html", status=500)

   - `lettings/views.py`:

     .. code-block:: python

        def index(request):
            lettings_list = Letting.objects.all()
            context = {"lettings_list": lettings_list}
            return render(request, "lettings/index.html", context)

        def letting(request, letting_id):
            letting = get_object_or_404(Letting, id=letting_id)
            logger.info(f"Accessing details of letting with ID: {letting_id}, Title: {letting.title}, "
                        f" Address: {letting.address}")
            context = {
                "title": letting.title,
                "address": letting.address,
            }
            return render(request, "lettings/letting.html", context)

   - `profiles/views.py`:

     .. code-block:: python

        def index(request):
            profiles_list = Profile.objects.all()
            context = {"profiles_list": profiles_list}
            return render(request, "profiles/index.html", context)

        def profile(request, username):
            profile = get_object_or_404(Profile, user__username=username)
            logger.info(f"Accessing profile details for username: {username}, Profile ID: {profile.id}")
            context = {"profile": profile}
            return render(request, "profiles/profile.html", context)

3. **Models**

   - `lettings/models.py`:

     .. code-block:: python

        class Address(models.Model):
            number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
            street = models.CharField(max_length=64)
            city = models.CharField(max_length=64)
            state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
            zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
            country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

            def __str__(self):
                return f"{self.number} {self.street}"

            class Meta:
                db_table = "oc_lettings_site_address"
                verbose_name_plural = "Addresses"

        class Letting(models.Model):
            title = models.CharField(max_length=256)
            address = models.OneToOneField(Address, on_delete=models.CASCADE)

            def __str__(self):
                return self.title

            class Meta:
                db_table = "oc_lettings_site_letting"

   - `profiles/models.py`:

     .. code-block:: python

        class Profile(models.Model):
            user = models.OneToOneField(User, on_delete=models.CASCADE)
            favorite_city = models.CharField(max_length=64, blank=True)

            def __str__(self):
                return self.user.username

            class Meta:
                db_table = "oc_lettings_site_profile"


User Guide
------------

1. **Access Home page**

The homepage of the site allows access to user information ("profiles") and property listings ("lettings") through two buttons.

   - Example URL: `http://localhost:8000/`

   .. image:: _static/home.png
      :alt: homepage screenshot
      :width: 600px
      :align: center

2. **Access User Profiles**

   On the homepage, click the **Profiles** button. You will be redirected to a page listing all user profiles.

   - Example URL: `http://localhost:8000/profiles/`

   .. image:: _static/profile.png
      :alt: profile screenshot
      :width: 600px
      :align: center

   - Example URL: `http://localhost:8000/profiles/DavWin/`

   .. image:: _static/profile_1.png
      :alt: profile example screenshot
      :width: 600px
      :align: center

3. **Access Property Listings**

   On the homepage, click the **Lettings** button. You will be redirected to a page listing all property listings.

   - Example URL: `http://localhost:8000/lettings/`

   .. image:: _static/lettings.png
      :alt: letting screenshot
      :width: 600px
      :align: center

   - Example URL: `http://localhost:8000/lettings/1/`

   .. image:: _static/lettings_1.png
      :alt: letting example screenshot
      :width: 600px
      :align: center

4. **Admin Page**

   The admin page allows adding or deleting profiles or lettings. To access the admin page, use the following credentials:

   - **Username**: admin
   - **Password**: Abc1234!

   - Example URL: `http://localhost:8000/admin/`

   .. image:: _static/admin.png
      :alt: admin authentication screenshot
      :width: 600px
      :align: center

   Once logged in, you can manage user profiles and property listings through the admin interface.

   .. image:: _static/admin_site.png
      :alt: admin interface screenshot
      :width: 600px
      :align: center

Deployment and Application Management Procedures
---------------------------------------------------

To correctly deploy the application on Render, you need to configure GitHub Actions with the following three environment variables: `DOCKER_PASSWORD`, `DOCKER_USERNAME`, and `SENTRY`.

**Set Up GitHub Actions**

In your GitHub repository settings, add the following secrets:

- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password.
- `SENTRY`: Your Sentry DSN (Data Source Name) for error tracking.

.. image:: _static/secrets_env.png
   :alt: GitHub Action secrets configuration screenshot
   :width: 600px
   :align: center

Once your GitHub Actions workflow is set up and the environment variables are configured, every push to the `main` branch will trigger the deployment process to Render. After a commit to the `main` branch, if all CI/CD criteria are met, the site is automatically redeployed on the Render hosting service at the following address: [https://openclassrooms.onrender.com/](https://openclassrooms.onrender.com/)

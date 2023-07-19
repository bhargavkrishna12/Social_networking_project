
- `social_networking_app`: This directory contains the Django app for the Social Networking functionalities.
  - `__pycache__/`: Cached Python files.
  - `migrations/`: Database migration files for the app's models.
  - `__init__.py`: Initialization file, makes the directory a Python package.
  - `admin.py`: Admin configuration for managing models in the Django admin site.
  - `apps.py`: App configuration.
  - `authentication.py`: Custom authentication classes (if any).
  - `models.py`: Django models for user, posts, comments, etc.
  - `serializers.py`: Django REST Framework serializers for API data serialization.
  - `tests.py`: Unit tests for the app.
  - `views.py`: Django views and API endpoints for handling HTTP requests.

- `social_networking_project`: This directory contains the project-level configuration and settings.
  - `db.sqlite3`: SQLite database file (or any other database file).
  - `docker-compose.yaml`: Docker Compose configuration to set up the development environment.
  - `manage.py`: Django's command-line utility for various tasks (e.g., running the development server, applying migrations).
  - `requirements.txt`: List of Python dependencies required to run the project.
  -

## How to Set Up and Run the Project

1. Install Python and Django:
   - Make sure you have Python (version 3.x) installed on your system. You can download it from https://www.python.org/downloads/.
   - Install Django and Django REST Framework:
     ```
     pip install django djangorestframework
     ```

2. Clone the repository

 
3. Install dependencies: using requirment.txt


4. Apply database migrations: python manage.py makemigrations , python manage.py migrate

5. Run the development server:  python manage.py runserver


6. Access the API:
- The development server is running at `http://localhost:8000/`.
- Use tools like Postman to interact with the API endpoints.

7.Install Docker and for running in docker environment.
----  docker build
----- docker-compose up



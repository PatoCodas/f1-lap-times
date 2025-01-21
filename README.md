# F1 Lap Times

## Description

The **F1 Lap Times** project is a web application developed in Django to record and visualize lap times for different Formula 1 tracks. It allows adding, viewing, and deleting lap times, and offers a dark mode for a better viewing experience.

## Features

- Add lap times for different tracks.
- View recorded lap times.
- Delete lap times.
- Toggle between light and dark mode.

## Dependencies

To run this project, you will need the following dependencies:

- Python 3.6+
- Django 3.2+
- djangorestframework 3.12.4
- Pillow 8.4.0

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PatoCodas/f1-lap-times.git
    cd f1-lap-times
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your browser:

    ```text
    http://127.0.0.1:8000/
    ```

## Project Structure

```filetree
f1-laptimes/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── laptimes/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_add_tracks.py
│   │   └── __init__.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── f1_lap_times.html
│   │   └── contact.html
├── manage.py
├── requirements.txt
└── .gitignore
```

# Contact

Email: miguelsilvaug@gmail.com
GitHub: PatoCodas


# Made with ❤️ by PatoCodas

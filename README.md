# Playingya
Playingya is a collaborative music playing app using Django &amp; React. It is being coded with help of [tutorials](https://www.youtube.com/playlist?list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j) from [Tech with Tim](https://www.youtube.com/c/TechWithTim).

# How to setup

1. Create a virtual environment using venv
    ```
    python3 -m venv venv
    ```
    and activate it
    ```
    source venv/bin/activate
    ```
2. Install requirements
    ```
    pip install -r requirements.txt
    ```
    or install modules with
    ```
    pip install django djangorestframework
    ```

# Cheat Sheet
- Start a django project called "music_controller"
    ```
    django-admin startproject music_controller
    ```
- Create a django app called "api" in our django project
    ```
    cd music_controller && django-admin startapp api
    ```
- Make migrations, whenever you make changes to the database or to a model, or to initialize the database
    ```
    ./manage.py makemigrations
    ```
    ```
    ./manage.py migrate
    ```
- Run the server
    ```
    ./manage.py runserver
    ```

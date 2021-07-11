# Journal Tool
A journaling web application built with [Django](https://www.djangoproject.com/).

## Demo App
You can see a demo version of the application deployed to [Heroku](https://www.heroku.com/) here: https://journal-tool.herokuapp.com/

## Functionality
Users can create entries in their journal to track events, mood, as well positive and negative thoughts. The application uses SQLite for development and PostgreSQL for deployment.

## Install Instructions
The application depends on Python, which can be installed and managed a variety of ways. For this project, I used [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv), following [this guide](https://realpython.com/intro-to-pyenv/).

Once Python is installed, install Django and dependencies using these commands:

`python -m pip install -r requirements.txt` - Install dependencies from [requirements.txt](/requirements.txt) file.

`python manage.py migrate` - Run migrations.

`python manage.py loaddata distortions.json` - Seed database with fixture for distortions (in [distortions.json](/journal/fixtures/distortions.json)).

`python manage.py runserver` - Run server.

If building for production, set these environment variables:

`export DATABASE_URL=<database_url>` - Configure a PostgreSQL database and insert url here.

`export DEBUG=FALSE` - Turn off debug mode for Django application.

`SECRET_KEY=<generate_secret_key>` - Insert a secret keye here. You can generate one using the Django library with the command: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

Then, to collect static files for production, run `python manage.py collectstatic`

## Project Structure
[`settings.py`](journaltool/settings.py) - Configuration settings for the application are stored here.

[`urls.py`](/journal/urls.py) - URL routes for the application are defined here.

[`views.py`](/journal/app.py) - Application (controller) logic is defined here. All routes are processed and requests are responded to.

[`models.py`](/journal/models.py) - Models are defined here using the [Django ORM](https://docs.djangoproject.com/en/3.2/topics/db/models/). This forms the basis for the database [migrations](/journal/migrations).

[`/templates`](/journal/templates/journal) - This directory contains all the templates (views) used by [views.py](/journal/views.py) to produce HTML responses to requests (with the help of [Django templating](https://docs.djangoproject.com/en/3.2/topics/templates/)).

[`/migrations`](/journal/migrations) - This directory contains the necessary files to migrate schema from the [models](/journal/models.py) file to the database (SQLite for development and PostgreSQL for deployment to Heroku).

[`/static`](/journal/static/journal) - All static files (CSS, JavaScript) are stored here.

[`/fixtures`](/journal/fixtures) - The seed files to initialize the database with data are stored here.

[`requirements.txt`](/requirements.txt) - This file is used by Python to keep track of the application's dependencies.

[`Procfile`](/Procfile) - Configuration for Heroku production deployment is stored here (which is set up to use [Gunicorn](https://gunicorn.org/)).

## Distinctiveness and Complexity

## More Info
This application began as the final project for Harvard's CS50 Web Programming course:
https://cs50.harvard.edu/web/2020/projects/final/capstone/.

## License
This project is open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
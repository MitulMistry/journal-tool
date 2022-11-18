# Journal Tool
![screenshot1](/readme/journal-tool_readme_01.png)

A journaling web application built with [Django](https://www.djangoproject.com/).

## Demo App
You can see a demo version of the application deployed to [Fly.io](https://fly.io/) here: https://journal-tool.fly.dev/

## Functionality
Users can create entries in their journal to track events, mood, as well positive and negative thoughts. It allows users to make complex journal entries involving events that take place during a day and linking them to cognitive distortions - or problems in the thinking that lead to poor mood - as well as negative thoughts that can be reframed and replaced by positive thoughts. In addition, statistics are calculated and sorted based on most common activities and distortions as entries are made. General mood level is tracked as well.

The application uses Django for the back end, Bootstrap, Font Awesome, and JavaScript for the front end, and SQLite for development, with PostgreSQL for deployment.

## Install Instructions
The application depends on Python, which can be installed and managed a variety of ways. For this project, I used [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv), following [this guide](https://realpython.com/intro-to-pyenv/).

Once Python is installed, install Django and dependencies using these commands:

`python -m pip install -r requirements.txt` - Install dependencies from [requirements.txt](/requirements.txt) file.

`export DATABASE_URL=<database_url>` - Configure a PostgreSQL database and insert url here.

`python manage.py migrate` - Run migrations.

`python manage.py loaddata distortions.json` - Seed database with fixture for distortions (in [distortions.json](/journal/fixtures/distortions.json)).

`python manage.py runserver` - Run server.

If building for production, set these environment variables:

`export DEBUG=FALSE` - Turn off debug mode for Django application.

`SECRET_KEY=<generate_secret_key>` - Insert a secret key here. You can generate one using the Django library with the command: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

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
![screenshot2](/readme/journal-tool_readme_02.png)

Journal Tool is a Django web application that leverages several models: users, entries, activities, and distortions. Journal entries can be made on a new entry form with functionality enhanced by JavaScript. Current time and date based on the browser's (client side) timezone are automatically selected (and can be modified). Activities can be created within the same form asynchronously without a page reload (leveraging internal API calls). Distortions are prepopulated using a [fixture file](/journal/fixtures/distortions.json) that must be applied. Distortions can be hovered over with tooltips appearing that give a brief summary of what the distortion means.

Once an entry is made, users can view truncated entries on a paginated entries page. An entry can be clicked on (using a "View more" link) with full entry visible on a new page. The entry can than be edited using the same form used to create the entry (with data automatically loaded).

![screenshot3](/readme/journal-tool_readme_03.png)

Going to the user profile page, data calculated based on the user's journal entries is presented. This includes the total count of distortions and activities that are collected over all of the user's entries (done so in class methods in the [models file](/journal/models.py)), sorted by highest to lowest. In addition, the total count of mood scores is queried via an API call and presented on a bar chart using [Chart.js](https://www.chartjs.org/).

Other features include the ability to edit activities and edit user data (including username, email, and password) via links on the user's profile page. The application utilizes Bootstrap for styling and templates, making the site mobile-responsive. Custom styling that overrides select Bootstrap styling is implemented in the [`styles.css`](journal/static/journal/styles.css) file.

## More Info
This application began as the final project for Harvard's CS50 Web Programming course:
https://cs50.harvard.edu/web/2020/projects/final/capstone/.

## License
This project is open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
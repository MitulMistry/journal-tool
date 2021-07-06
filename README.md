# Journal Tool
A journaling web application built with Django.

## Demo App
You can see a demo version of the application deployed to Heroku here: https://journal-tool.herokuapp.com/

## Functionality
Users can create entries in their journal to track events, mood, as well positive and negative thoughts.

## Install Instructions
The application depends on Python, which can be installed and managed a variety of ways. For this project, I used [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv), following [this guide](https://realpython.com/intro-to-pyenv/).

`python -m pip install -r requirements.txt` - Install dependencies from [requirements.txt](/requirements.txt) file.
`python manage.py migrate` - Run migrations.
`python manage.py loaddata distortions.json` - Seed database with fixture for distortions (in [distortions.json](/journal/fixtures/distortions.json)).
`python manage.py runserver` - Run server.

## Project Structure

## Distinctiveness and Complexity

## More Info
This application began as the final project for Harvard's CS50 Web Programming course:
https://cs50.harvard.edu/x/2021/project/.

## License
This project is open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
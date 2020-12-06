# CollegeDreaming

A Django application for senior design.

## Description

A web application that targets college students, adults seeking a degree, and high school students and their families.

## Technologies Used

- HTML
- CSS
- JavaScript
- JQuery
- Python
  - Django Framework (including Django template engine)
- SQL

## Unique Problems Faced & How They Were Fixed

- pip install mysqlclient
  - [https://github.com/PyMySQL/mysqlclient-python#install](https://github.com/PyMySQL/mysqlclient-python#install)
- Chart.js being too responsive
  - Charts were extremely small on mobile screens, in order to fix this you must set "maintainAspectRatio" to false in your chart's options, wrap your charts in a div and then use media queries to set the new div's pixel dimensions.

## Useful Terminal Commands
- Python manage.py runserver
  - Will start the application on localhost
- Python manage.py makemigrations
  - Use this when creating/editing models
- Python manage.py migrate
  - Use this after running "Python manage.py makemigrations"

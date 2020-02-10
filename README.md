# Assignment

Create a RESTful API that would help your team decide on groups of people who are eligible for
various upcoming government grants.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

A step by step series of examples that tell you how to get the development env running

Step 1: Activate the virtual environment

```
source env/bin/activate
```

Step 2: Install Django framework

```
pip3 install django
```

Step 3: Make migrations and migrate

```
python manage.py makemigrations
python manage.py migrate
```

Step 4: Create an user for database (http://127.0.0.1:8000/admin)

```
python manage.py createsuperuser
```

Step 5: Run the server

```
python manage.py runserver
```

Step 6: Run the server

```
Go to http://127.0.0.1:8000/admin and login using the user that you've created at Step 4. 
And you will be able to view the data and records that are added into the database from the admin page.
```

## Built With

* [Python 3.7](https://www.python.org/downloads/) - The programming language used
* [Django 3.0.3](https://docs.djangoproject.com/en/3.0/releases/3.0.3/) - The framework used

## Endpoints

* Create household: http://127.0.0.1:8000/api/household/create/
* Add a family member to household: http://127.0.0.1:8000/api/household/add/
* List households: http://127.0.0.1:8000/api/household/
* Show the details of a household: http://127.0.0.1:8000/api/household/[id]/
* Delete household: http://127.0.0.1:8000/api/household/[id]/delete/
  

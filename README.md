# REST API serving a cake splitting algorithm

This API is a RESTful CRUD to serve an algorithm designed to identify the smallest repeating sequence in a string.

Ex: for string "ababab", the smallest repeating sequence is "ab"

It uses the Cerberus package for simple validation of input, and is persisted to sqlite.

# Requirements and Installation

Python 3.7.2
Django 3.0

(virtual env)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

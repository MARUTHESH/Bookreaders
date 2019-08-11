# Bookreaders
This is the project developed using python and Django web framework. This web application is used to help the reader by managing the reader list by adding new books, editing the existing book, editing the status, deleting the book. This app also provide api to add, delete, update and listing of the added books.

## Python setup

On Linux, execute the following commands (first time setup)
1. python --version
2. lsvirtualenv
3. mkvirtualenv bookreadersapp --python=python3
4. python --version
5. pip install -r requirements.txt

## Running the project
1. python manage.py migrate
2. python manage.py runserver 0:8000

## Create the user
1. python manage.py createsuperuser

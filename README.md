chucho-demo
===========

A demo application using the django-chucho module for object management


GETTING STARTED
---------------

1) Setup submodules by running the following at the root of the application.

    git submodule update --init --recursive


2) Setup database with inital data.
    
    ./manage.py setup

    This loads one super user with the following credentials to login with:
        username - super@demo.com
        password - password

3) Start Django server.
    
    ./manage.py runserver localhost:8000

    Now you can go to the address "localhost:8000" in your browser to start using the demo application.

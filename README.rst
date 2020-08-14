ml_with_django
==================

**ml_with_django** is a opensource template for serving machine learning model with django application. This project also contains a almost production-ready admin dashboard, which is based on django-admin.

You can use this template for developing django based ml-application very quickly only with several steps.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


.. contents:: **Contents of this document**
   :depth: 3


Settings (TBD)
----------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Pre-installation
----------------

* python 3.6.5

* pip

* virtualenv  or virtualwrapper

Setting up your admin user and getting started
------------------------------------------------

* By default setting Django will create a local sqllite.db and use this database for local development.

* Create a **superuser account**, and start application::

    $ mkvirtualenv <project_name>   # create a new python virutal environment
    $ workon <project_name>         # active this environment
    $ pip install -r requirements   # install project dependencies -> it will take a few minutes, depends on your network...
    $ python manage.py makemigrations
    $ python manage.py migrate  # create admin tables
    $ python manage.py createsuperuser --settings=config.settings.local # create local admin user -> enter username, email and password here!
    $ python manage.py runserver 127.0.0.1:8000 # start local service

* For creating **new user account**, just sign up with admin account and create a new group by using /admin UI and add new user to this group. 
Once you submit it, the user should be verified and ready to use.



Project structure
--------------------------

apps
^^^^^^^^

It contains main program logic. All of packages here must follow MTV-Design-Pattern (Model, Template, View). 

**users** provides a customized user-login and user management

**image_inf** is a example program for car damage classification
ref_

.. _ref: https://github.com/gaetjen/capstone_webapp


config
^^^^^^^^^^

This folder contains django url, wsgi settings.<br>
You can inherit base.py for test or production deployment scope.

extra_apps
^^^^^^^^^^^^
third party program and plugins

media
^^^^^^^^
Place for storing images, audio, video files on your local filesystem.
Subfolder **models** contains pretrained ML-Models.

ml_with_django
^^^^^^^^^^^^^^^^
Place for storing frontend template

requirements
^^^^^^^^^^^^^^
Place for dependency settings.

staticfiles
^^^^^^^^^^^^^^^
stores frontend static template like css, html, js for webserver.

    $ python manage.py collectstatic

Test coverage (TBD)
---------------------

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test (TBD)
--------------------------------

::

  $ py.test


Sentry (TBD)
----------------

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Screenshot
----------------


Admin Backend for Image Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/xiabai84/ml_with_django/master/screenshot/customer_image.png
    :alt: HTTPie in action
    :width: 100%
    :align: center



Log Management
^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/xiabai84/ml_with_django/master/screenshot/log_management.png
    :alt: HTTPie in action
    :width: 100%
    :align: center



Screenshot for User and Group Permission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/xiabai84/ml_with_django/master/screenshot/group_permissions.png
    :alt: HTTPie in action
    :width: 100%
    :align: center

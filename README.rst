ml_with_django
==================

**ml_with_django** project provides a template for serving machine learning model with django (python) backend. This project also contains a almost production-ready Admin-Management-UI, which is enhanced default django-admin UI.

You can use this template to develop a django project very quickly with several steps.

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

    python 3.6.5

    pip

    virtualenv

    virtualwrapper

Setting up your admin user and getting started
------------------------------------------------

* By default setting without any configuration for database... Django will create a sqllite.db for us. This program will use this database for local development.

* Create an **superuser account**, and start this django program::

    $ workon <project_name> / $ mkvirtualenv <project_name>
    $ pip install -r requirements
    $ python manage.py makemigrations
    $ python manage.py migrate  # create admin tables
    $ python manage.py createsuperuser --settings=config.settings.local # create local admin user -> enter username, email and password here!
    $ python manage.py runserver 127.0.0.1:8000 # start local service

* To create a **normal user account**, just sign up with your admin account and create a new group by using /admin UI and add a new user to this group. Once you submit it, the user should be verified and ready to use.



Project structure
--------------------------

apps
^^^^^^^^

    Main program logic

    users provides a customized user-login and user management

    image_info is a example program for car damage classification
    ref_

.. _ref: https://github.com/gaetjen/capstone_webapp


config
^^^^^^^^^^

    contains django url, wsgi (local mode by default) settings
    sub-folder settings contains configuration parameters for settings (django setting.py). You can inherit base.py for test or production deployment configuration.

extra_apps
^^^^^^^^^^^^
    third party program and plugins

media
^^^^^^^^
    Place for storing images, audio, video files
    In Sub folder **models** stores trained ML-Models

ml_with_django
^^^^^^^^^^^^^^^^
    Place for storing frontend template

requirements
^^^^^^^^^^^^^^
    manages project's dependencies.

staticfiles
^^^^^^^^^^^^^^^
    stores frontend static template for webserver or a third-party file storage (nginx).

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

    SYou must set the DSN url in production.


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

.. _install_development:

=======================
Development environment
=======================

Quick start
===========

#. Navigate to the location where you want to place your project.

#. Get the code::

    $ git clone git@bitbucket.org:maykinmedia/openpersonen.git
    $ cd openpersonen

#. Install all required libraries:

    .. code-block:: bash

       $ virtualenv env
       $ source env/bin/activate
       $ pip install -r requirements/dev.txt

#. Activate your virtual environment and create the statics and database::

    $ source env/bin/activate  # or, workon <env> if you use virtualenvwrapper
    $ npm install
    $ gulp sass
    $ python src/manage.py collectstatic --link
    $ python src/manage.py migrate


Next steps
----------

Optionally, you can load demo data and extract demo media files::

    $ python src/manage.py loaddata demo
    $ cd media
    $ tar -xzf demo.tgz

You can now run your installation and point your browser to the address given
by this command::

    $ python src/manage.py runserver

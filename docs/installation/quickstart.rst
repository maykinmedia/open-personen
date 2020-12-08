.. _installation_quickstart:

Quickstart
==========

.. warning::
    The quickstart instructions are only intended for development and testing purposes.
    Do not use the quickstart instructions in a production setting.
    The certificate and certificate key stored in the StUF-BG Client will be exposed
    when making an API call to an external StUF-BG service.


The default ``docker-compose`` settings have some convenience settings to get
started quickly and these should never be used for anything besides testing:

* A default secret is set in the ``SECRET_KEY`` environment variable
* A predefined database and database account is used.
* The demo data source is used as backend.
* API authorizations are disabled.

With the above remarks in mind, let's go:

1. Download the ``docker-compose`` file:

   .. tabs::

      .. tab:: Linux

         .. code:: shell

            $ wget https://raw.githubusercontent.com/maykinmedia/open-personen/master/docker-compose-quickstart.yml -O docker-compose.yml

      .. tab:: Windows Powershell 3

         .. code:: shell

            PS> wget https://raw.githubusercontent.com/maykinmedia/open-personen/master/docker-compose-quickstart.yml -Odocker-compose.yml

2. Start the Docker containers:

   .. code:: shell

      $ docker-compose up -d

3. Import a test dataset of persons. You can use the test dataset provided by
   the `RvIG`_. Just copy the ODS-file URL to the command below:

   .. code:: shell

      $ docker-compose exec web src/manage.py import_demodata --url <url>

4. The API should now be available on ``http://localhost:8000/api/``. You can
   retrieve a person via the BRP API in your webbrowser:

   .. code::

      http://localhost:8000/api/ingeschrevenpersonen/999990676

.. _`RvIG`: https://www.rvig.nl/documenten/richtlijnen/2018/09/20/testdataset-persoonslijsten-proefomgevingen-gba-v


Next steps
----------

You can read how to add persons to this test dataset using this
:ref:`backends_demo_backend`. If you want to expose real persons you can connect
Open Personen to a :ref:`backends_stufbg_backend`.

You can also read on how to enable :ref:`installation_authorizations`.

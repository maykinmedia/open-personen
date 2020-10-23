.. _installation_quickstart:

Quickstart
==========

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

4. Retrieve a person via the BRP API in your webbrowser:

   .. code:: 

      http://localhost:8000/api/ingeschrevenpersonen/999990676/

.. _`RvIG`: https://www.rvig.nl/documenten/richtlijnen/2018/09/20/testdataset-persoonslijsten-proefomgevingen-gba-v

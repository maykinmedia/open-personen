.. _backends_stufbg_backend:

StUF-BG backend
===============

This backend allows Open Personen to connect to a StUF-BG compatible service to
retrieve person data.

Installation
------------

Any backend change requires a change in the 
:ref:`environment <installation_environment_config>` that are present when 
the application is launched. Add this setting to use the StUF-BG backend:

.. code:: bash

    OPENPERSONEN_BACKEND=openpersonen.contrib.stufbg.backend.default

The StUF-BG backend requires authorizations to be enabled. You can do this by
setting:

.. code:: bash

    OPENPERSONEN_USE_AUTHENTICATION=True

Configuration
-------------

The StUF-BG backend requires you to setup some connection settings within the
admin interface of Open Personen.

1. If you haven't done so already, make a superuser account to login to the 
   admin:

   .. tabs::

      .. tab:: Development

         .. code:: shell

            $ python src/manage.py createsuperuser

      .. tab:: Docker

         .. code:: shell

            $ docker-compose exec web src/manage.py createsuperuser

2. Point your webbrowser to the admin interface, for example:
   ``http://localhost:8000/admin/``

3. Login with the username and password from step 1.

4. Navigate to *StUF-BG backend* > *StUF-BG Client*

5. Fill in all relevant fields and click on *OPSLAAN*.


Next steps
----------

You can continue to read how to enable :ref:`installation_authorizations`.


In depth
--------

.. toctree::
   :maxdepth: 1

   implementation

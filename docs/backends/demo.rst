.. _backends_demo_backend:

Demo backend
============

This backend provides a local testset of persons to use for testing purposes.
No external service is needed, all data is stored and retrieved a from the
local database.

Installation
------------

Any backend change requires a change in the 
:ref:`environment <installation_environment_config>` that are present when 
the application is launched. Add this setting to use the Demo backend:

.. code:: bash

    OPENPERSONEN_BACKEND=openpersonen.contrib.demo.backend.default

Configuration
-------------

The demo backend does not require any additional configuration but you probably
want to load a predefined testset of persons or you can create test persons
yourself.

Import testset
~~~~~~~~~~~~~~

An `example testset`_ can be found on the 
`Rijksdienst voor Identiteitsgegevens`_ (RvIG) website. You can load this set 
directly into the demo backend.

.. tabs::

   .. tab:: Development

      .. code:: shell

        $ python src/manage.py import_demodata --url=<testset url>

   .. tab:: Docker

      .. code:: shell

        $ docker-compose exec web src/manage.py import_demodata --url=<testset url>

.. _`example testset`: https://www.rvig.nl/documenten/richtlijnen/2018/09/20/testdataset-persoonslijsten-proefomgevingen-gba-v
.. _`Rijksdienst voor Identiteitsgegevens`: https://www.rvig.nl/

**Example data**

To give you some quick insights in the testset that is provided, here's a 
family tree present in this testset:

* C\.F. Wiegman (``999990676``) *partner of* A.H. Holthuizen (``999990421``), *children*:

  * A\. Holthuizen (``999991978``) *no partner*

    * *no children*

  * A\.F. Holthuizen (``999991760``) *no partner*

    * *no children*

  * M\. du Burck-Holthuizen (``999993392``) *partner of* J.L. du Burck (``999991589``), *children*:

    * M\. du Burck (``999991115``) *no partner*

      * *no children*

    * C\. Djibet-du Burck (``999992223``) *partner of* R. Djibet (``999994347``), *children*:

      * N\.Q. Djibet (``999994281``) *no partner*

        * *no children*

      * F\.Z. Djibet (``999993264``) *no partner*

        * *no children*

      * N\.H. Djibet (``999994177``) *partner of* K.S.A. Bronwaßer (``999995224``), *children*:

        * R\.S. Bronwasser (``999992612``)


Create test persons
~~~~~~~~~~~~~~~~~~~

When using the demo backend you can create and delete persons freely. The 
management interface allows you to create, update and delete persons and manage
their basic properties. This can be usefull when using predefined BSNs in a 
test environment that don't match up with an existing testset or if you want to
test specific field values or relations between persons.

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

4. Navigate to *Demo backend* > *Personen*

5. You can edit, create or delete persons that become available via the API.


Next steps
----------

You can continue to read how to enable :ref:`installation_authorizations`.
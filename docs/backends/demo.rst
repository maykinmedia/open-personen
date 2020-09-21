Demo backend
============

This backend provides a local testset of persons to use for testing purposes.
No external service is needed, all data is stored and retrieved a from the
local database.

Installation
------------

Any backend change requires a change in the environment or Python settings that 
are present when the application is launched.

.. code:: bash

    OPENPERSONEN_BACKEND=openpersonen.backends.demo

Configuration
-------------

The demo backend does not require any additional configuration but you probably
want to load a predefined testset of persons.

An `example testset`_ can be found on the 
`Rijksdienst voor Identiteitsgegevens`_ (RvIG) website. You can load this set 
directly into the demo backend.

You can do this with a management command, for development:

.. code:: shell

    $ python src/manage.py import_demodata <testset file or url>

or, when running in a Docker-container:

.. code:: shell

    $ docker-compose exec web src/manage.py import_demodata <testset file or url>

.. _`example testset`: https://www.rvig.nl/documenten/richtlijnen/2018/09/20/testdataset-persoonslijsten-proefomgevingen-gba-v
.. _`Rijksdienst voor Identiteitsgegevens`: https://www.rvig.nl/

Example data
------------

To give you some quick insights in the testset that is provided, here's a 
family tree present in this testset:

* C\.F. Wiegman (`999990676`) *partner of* A.H. Holthuizen (`999990421`), *children*:

  * A\. Holthuizen (`999991978`) *no partner*

    * *no children*

  * A\.F. Holthuizen (999991760) *no partner*

    * *no children*

  * M\. du Burck-Holthuizen (`999993392`) *partner of* J.L. du Burck (`999991589`), *children*:

    * M\. du Burck (`999991115`) *no partner*

      * *no children*

    * C\. Djibet-du Burck (`999992223`) *partner of* R. Djibet (`999994347`), *children*:

      * N\.Q. Djibet (`999994281`) *no partner*

        * *no children*

      * F\.Z. Djibet (`999993264`) *no partner*

        * *no children*

      * N\.H. Djibet (`999994177`) *partner of* K.S.A. Bronwaßer (`999995224`), *children*:

        * R\.S. Bronwasser (`999992612`)
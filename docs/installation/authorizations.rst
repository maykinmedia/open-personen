.. _installation_authorizations:

Authorizations
==============

Open Personen uses API-tokens as authorizations mechanism. You can connect an
API-token to a user for identification.

Any backend change requires a change in the 
:ref:`environment <installation_environment_config>` that are present when 
the application is launched. Add this setting to enable authorizations:

.. code:: bash

    OPENPERSONEN_USE_AUTHENTICATION=True

Manage API tokens
-----------------

You can manage API-tokens in the admin interface or create tokens from the
command line.

1. Point your webbrowser to the admin interface, for example:
   ``http://localhost:8000/admin/``

2. Login with the username and password of a superuser (see 
   :ref:`installation_quickstart`).

3. Navigate to *API Autorisaties* > *Tokens*

4. Click on *Token toevoegen*

5. Select a *Gebruiker* to link the API token to an existing user. Click 
   on *Opslaan en opnieuw bewerken*.

6. The *Key* field should now have a value like 
   ``e5640c8bde0b9b1a168595d798df721ef12bbbef``

7. You can now make API calls using this API-token. For example:

   .. code:: shell

      $ curl -i -H "Accept: application/json" -H "Authorization: Token e5640c8bde0b9b1a168595d798df721ef12bbbef" http://localhost:8000/api/ingeschrevenpersonen/999990676

   You can not access the API from your browser anymore, since you need to pass
   the proper authorization header.

8. You can also create API-tokens from the command line:

   .. tabs::
   
      .. tab:: Development
   
         .. code:: shell
   
            $ python src/manage.py generate_token demo
            Generated token: e5640c8bde0b9b1a168595d798df721ef12bbbef
   
      .. tab:: Docker
   
         .. code:: shell
   
            $ docker-compose exec web src/manage.py generate_token demo
            Generated token: e5640c8bde0b9b1a168595d798df721ef12bbbef

   This causes a user ``demo`` to be created with the generated token. By 
   default, this user has no permission to access the admin interface.

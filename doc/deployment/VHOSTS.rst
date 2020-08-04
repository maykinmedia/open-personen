Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess openpersonen-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/openpersonen/log/apache2/error.log"
        CustomLog "/srv/sites/openpersonen/log/apache2/access.log" common

        WSGIProcessGroup openpersonen-<target>

        Alias /media "/srv/sites/openpersonen/media/"
        Alias /static "/srv/sites/openpersonen/static/"

        WSGIScriptAlias / "/srv/sites/openpersonen/src/openpersonen/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-openpersonen-<target>]
    user = <user>
    command = /srv/sites/openpersonen/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/openpersonen/src/openpersonen/wsgi/wsgi_<target>.py
    home = /srv/sites/openpersonen/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/openpersonen/log/uwsgi_err.log
    stdout_logfile = /srv/sites/openpersonen/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_openpersonen_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/openpersonen/log/nginx-access.log;
      error_log /srv/sites/openpersonen/log/nginx-error.log;

      location /500.html {
        root /srv/sites/openpersonen/src/openpersonen/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/openpersonen/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/openpersonen/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_openpersonen_<target>;
      }
    }

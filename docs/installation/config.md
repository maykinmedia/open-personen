# Environment configuration reference

Open Personen can be ran both as a Docker container or directly on a VPS or
dedicated server. It relies on other services, such as database and cache
backends, which can be configured through environment variables.

## Available environment variables

### Required

* `DJANGO_SETTINGS_MODULE`: which environment settings to use. Available options:
  - `openpersonen.conf.docker`
  - `openpersonen.conf.dev`
  - `openpersonen.conf.ci`

* `SECRET_KEY`: secret key that's used for certain cryptographic utilities. You
  should generate one via
  [miniwebtool](https://www.miniwebtool.com/django-secret-key-generator/)

* `ALLOWED_HOSTS`: a comma separated (without spaces!) list of domains that
  serve the installation. Used to protect against `Host` header attacks.

### Optional

* `SITE_ID`: defaults to `1`. The database ID of the site object. You usually
  won't have to touch this.

* `DEBUG`: defaults to `False`. Only set this to `True` on a local development
  environment. Various other security settings are derived from this setting!

* `IS_HTTPS`: defaults to the inverse of `DEBUG`. Used to construct absolute
  URLs and controls a variety of security settings.

* `DB_HOST`: hostname of the PostgreSQL database. Defaults to `localhost`,
  unless you're using the `docker` environment, then it defaults to `db`.

* `DB_USER`: username of the database user. Defaults to `openzaak`,
  unless you're using the `docker` environment, then it defaults to `postgres`.

* `DB_PASSWORD`: password of the database user. Defaults to `openzaak`,
  unless you're using the `docker` environment, then it defaults to no password.

* `DB_NAME`: name of the PostgreSQL database. Defaults to `openzaak`,
  unless you're using the `docker` environment, then it defaults to `postgres`.

* `DB_PORT`: port number of the database, defaults to `5432`.

* `SENTRY_DSN`: URL of the sentry project to send error reports to. Default
  empty, i.e. -> no monitoring set up. Highly recommended to configure this.

* `OPENPERSONEN_BACKEND`: The data source to use for obtaining person data. Can
  be any of the values below:

  * `openpersonen.contrib.demo.backend.default` (default)
  * `openpersonen.contrib.stufbg.backend.default`

* `OPENPERSONEN_USE_AUTHENTICATION`. Require an API-token to access the API.
  Defaults to `True` (but set to `False` in our `docker-compose.yml`)

## Specifying the environment variables

There are two strategies to specify the environment variables:

* provide them in a `.env` file
* start the Open Zaak processes (with uwsgi/gunicorn/celery) in a process
  manager that defines the environment variables

### Providing a .env file

This is the most simple setup and easiest to debug. The `.env` file must be
at the root of the project - i.e. on the same level as the `src` directory (
NOT _in_ the `src` directory).

The syntax is key-value:

```
SOME_VAR=some_value
OTHER_VAR="quoted_value"
```

### Provide the envvars via the process manager

If you use a process manager (such as supervisor/systemd), use their techniques
to define the envvars. The Open Zaak implementation will pick them up out of
the box.

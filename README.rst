=============
Open Personen
=============

:Version: 0.1.0
:Source: https://github.com/maykinmedia/open-personen
:Keywords: Basisregistratie personen, BRP, VNG, StUF-BG, Common Ground
:PythonVersion: 3.7

|build-status| |docs| |coverage| |black| |docker|

A modern Basisregistratie Personen (BRP) API to retrieve personal data.
(`Nederlandse versie`_)

Developed by `Maykin Media B.V.`_.


Introduction
============

An implementation of the `Haal Centraal BRP bevragen API specification`_ using
a `StUF-BG`_ connection to access locally stored personal data via mondern REST
API.

Open Personen meets the need for several other components to request personal 
data and to link persons (e.g. to a zaak in the `Open Zaak`_). A so-called 
Profile API is also available where additional, non-authentic, personal data 
can be stored such as phone number and email address.

.. _`Haal Centraal BRP bevragen API specification`: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen
.. _`StUF-BG`: https://www.gemmaonline.nl/index.php/Sectormodel_Basisgegevens:_StUF-BG
.. _`Open Zaak`: https://open-zaak.readthedocs.io/


References
==========

* `Issues <https://github.com/maykinmedia/open-personen/issues>`_
* `Code <https://github.com/maykinmedia/open-personen>`_
* `Community <https://commonground.nl/groups/view/54477955/open-personen>`_
* `Documentation <https://open-personen.readthedocs.io/>`_

Licence
=======

Copyright © Maykin Media B.V., 2020

Licensed under the `Business Source License`_ (BSL) 1.1

* `Why this license?`_ :bulb: 

.. _`Why this license?`: https://open-personen.readthedocs.io/en/latest/introduction/source-code/why-bsl.html

.. _`Nederlandse versie`: README.NL.rst

.. _`Maykin Media B.V.`: https://www.maykinmedia.nl

.. _`Business Source License`: LICENSE.md

.. |build-status| image:: https://travis-ci.org/maykinmedia/open-personen.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/maykinmedia/open-personen

.. |docs| image:: https://readthedocs.org/projects/open-personen/badge/?version=latest
    :target: https://open-personen.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |coverage| image:: https://codecov.io/github/maykinmedia/open-personen/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage
    :target: https://codecov.io/gh/maykinmedia/open-personen

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |docker| image:: https://images.microbadger.com/badges/image/maykinmedia/open-personen.svg
    :target: https://hub.docker.com/r/maykinmedia/open-personen

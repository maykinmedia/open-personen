=============
Open Personen
=============

:Version: 0.1.0
:Source: https://github.com/maykinmedia/open-personen
:Keywords: Basisregistratie personen, BRP, VNG, StUF-BG, Common Ground
:PythonVersion: 3.7

|build-status| |docs| |coverage| |black| |docker|

Een moderne Basisregistratie Personen (BRP) API voor het bevragen van 
persoonsgegevens. (`English version`_)

Ontwikkeld door `Maykin Media B.V.`_.


Introductie
===========

Een implementatie van de `Haal Centraal BRP bevragen API specificatie`_ met 
`StUF-BG`_ koppeling voor het ontsluiten van lokale persoonsgegevens via een 
moderne REST API.

Open Personen voorziet in de behoefte van verschillende andere componenten om 
persoonsgegevens op te vragen en personen te koppelen (bijv. aan een zaak in 
de `Open Zaak`_). Tevens is een zogenoemde Profiel API beschikbaar waar 
additionele, niet-authentieke, persoonsgegevens in kunnen worden opgeslagen 
zoals telefoonnummer en e-mailadres.

.. _`Haal Centraal BRP bevragen API specificatie`: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen
.. _`StUF-BG`: https://www.gemmaonline.nl/index.php/Sectormodel_Basisgegevens:_StUF-BG
.. _`Open Zaak`: https://open-zaak.readthedocs.io/


Links
=====

* `Issues <https://github.com/maykinmedia/open-personen/issues>`_
* `Code <https://github.com/maykinmedia/open-personen>`_
* `Community <https://commonground.nl/groups/view/54477963/objecten-en-objecttypen-api>`_


Licentie
========

Copyright © Maykin Media B.V., 2020

Licensed under the `Business Source License`_ (BSL) 1.1


.. _`English version`: README.rst

.. _`Maykin Media B.V.`: https://www.maykinmedia.nl

.. _`Business Source License`: LICENCE.md

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
    :target: https://microbadger.com/images/maykinmedia/open-personen

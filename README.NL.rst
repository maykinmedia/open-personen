=============
Open Personen
=============

:Version: 0.1.0
:Source: https://github.com/maykinmedia/open-personen
:Keywords: Basisregistratie personen, BRP, VNG, StUF-BG, Common Ground
:PythonVersion: 3.7

|code-quality| |build-status| |coverage| |black| |docker| |python-versions|

Een moderne Basisregistratie Personen (BRP) API voor het bevragen van
persoonsgegevens. (`English version`_)

Ontwikkeld door `Maykin Media B.V.`_.


Introductie
===========

Open Personen biedt een implementatie van de
`Haal Centraal BRP bevragen API specificatie`_ en kan verbinden met een
`StUF-BG`_ koppeling voor het ontsluiten van persoonsgegevens. Ook kan Open
Personen eenvoudigweg StUF-BG berichten converteren naar BRP API berichten
zonder daadwerkelijke verbinding. Ten slotte kan Open Personen gebruikt worden
met een testset die u kunt importeren of zelf aanmaken via de gebruikers
interface.

Open Personen voorziet in de behoefte van verschillende andere componenten om
persoonsgegevens op te vragen en personen te koppelen (bijv. aan een zaak in
de `Open Zaak`_).

.. _`Haal Centraal BRP bevragen API specificatie`: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen
.. _`StUF-BG`: https://www.gemmaonline.nl/index.php/Sectormodel_Basisgegevens:_StUF-BG
.. _`Open Zaak`: https://open-zaak.readthedocs.io/


Links
=====

* `Documentatie <https://open-personen.readthedocs.io/>`_
* `Docker image <https://hub.docker.com/r/maykinmedia/open-personen>`_
* `Issues <https://github.com/maykinmedia/open-personen/issues>`_
* `Code <https://github.com/maykinmedia/open-personen>`_
* `Community <https://commonground.nl/groups/view/54477955/open-personen>`_


Licentie
========

Copyright © Maykin Media B.V., 2020

Licensed under the `Business Source License`_ (BSL) 1.1

* `Waarom deze licentie?`_ :bulb:

.. _`Waarom deze licentie?`: https://open-personen.readthedocs.io/en/latest/introduction/source-code/why-bsl.html

.. _`English version`: README.rst

.. _`Maykin Media B.V.`: https://www.maykinmedia.nl

.. _`Business Source License`: LICENSE.md

.. |code-quality| image:: https://github.com/maykinmedia/open-personen/workflows/Code%20Quality/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/open-personen/actions

.. |build-status| image:: https://github.com/maykinmedia/open-personen/workflows/Continuous%20Integration/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/open-personen/actions

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

.. |python-versions| image:: https://img.shields.io/badge/python-3.7%2B-blue.svg
    :alt: Supported Python version

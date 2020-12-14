=============
Open Personen
=============

:Version: 0.1.0
:Source: https://github.com/maykinmedia/open-personen
:Keywords: Basisregistratie personen, BRP, VNG, StUF-BG, Common Ground
:PythonVersion: 3.7

|build-status| |code-quality| |docs| |coverage| |black| |docker| |python-versions|

A modern Basisregistratie Personen (BRP) API to retrieve personal data.
(`Nederlandse versie`_)

Developed by `Maykin Media B.V.`_.


Introduction
============

Open Personen offers an implementation of the 
`Haal Centraal BRP bevragen API specification`_ and can connect to a `StUF-BG`_ 
service to retrieve personal data. In addition, Open Personen can simply convert
StUF-BG messages to BRP API messages without an actual connection. Finally, you 
can use Open Personen with a test set that you either import or construct 
yourself via the user interface.

Open Personen meets the need for several other components to request personal 
data and to link persons (e.g. to a zaak in the `Open Zaak`_). 

.. _`Haal Centraal BRP bevragen API specification`: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen
.. _`StUF-BG`: https://www.gemmaonline.nl/index.php/Sectormodel_Basisgegevens:_StUF-BG
.. _`Open Zaak`: https://open-zaak.readthedocs.io/


References
==========

* `Documentation <https://open-personen.readthedocs.io/>`_
* `Docker image <https://hub.docker.com/r/maykinmedia/open-personen>`_
* `Issues <https://github.com/maykinmedia/open-personen/issues>`_
* `Code <https://github.com/maykinmedia/open-personen>`_
* `Community <https://commonground.nl/groups/view/54477955/open-personen>`_


Licence
=======

Copyright © Maykin Media B.V., 2020

Licensed under the `Business Source License`_ (BSL) 1.1

* `Why this license?`_ :bulb: 

.. _`Why this license?`: https://open-personen.readthedocs.io/en/latest/introduction/source-code/why-bsl.html

.. _`Nederlandse versie`: README.NL.rst

.. _`Maykin Media B.V.`: https://www.maykinmedia.nl

.. _`Business Source License`: LICENSE.md

.. |build-status| image:: https://github.com/maykinmedia/open-personen/workflows/Continuous%20Integration/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/open-personen/actions

.. |code-quality| image:: https://github.com/maykinmedia/open-personen/workflows/Code%20Quality/badge.svg
    :alt: Code quality
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

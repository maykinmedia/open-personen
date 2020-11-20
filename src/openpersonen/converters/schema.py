from drf_yasg import openapi

description = """
API voor het converteren van Open Personen API-verzoeken naar StUF-BG-verzoeken en
StUF-BG-antwoorden naar Open Personen API-antwoorden.

Deze API geen externe verzoeken of data manipulatie te doen, zet het alleen data tussen verschillende formaten.
"""


info = openapi.Info(
    title="Converteren ingeschreven personen",
    default_version="1.0.0",
    description=description,
    contact=openapi.Contact(
        email="support@maykinmedia.nl", url="https://www.maykinmedia.nl"
    ),
    license=openapi.License(
        name="EUPL 1.2", url="https://opensource.org/licenses/EUPL-1.2"
    ),
)

from drf_yasg import openapi

description = """
API voor het ontsluiten van gegevens van ingeschreven personen en aanverwante gegevens uit de GBA en RNI.
Met deze API worden de actuele gegevens van ingeschreven personen, hun kinderen, partners en ouders ontsloten.

Heeft een persoon bijvoorbeeld geen geldige nationaliteit, dan wordt nationaliteit niet geretourneerd.

Heeft een persoon een beëindigd partnerschap of huwelijk, dan wordt de partner niet geretourneerd.
"""


info = openapi.Info(
    title="Bevragingen ingeschreven personen",
    default_version="1.0.0",
    description=description,
    contact=openapi.Contact(
        email="support@maykinmedia.nl", url="https://www.maykinmedia.nl"
    ),
    license=openapi.License(
        name="EUPL 1.2", url="https://opensource.org/licenses/EUPL-1.2"
    ),
)

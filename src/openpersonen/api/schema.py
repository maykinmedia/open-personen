from drf_yasg import openapi


description = "Open Personen Schema"


info = openapi.Info(
    title="Besluiten API",
    default_version='1.0.0',
    description=description,
    contact=openapi.Contact(
        email='support@maykinmedia.nl', url='https://www.maykinmedia.nl'
    ),
    license=openapi.License(
        name="EUPL 1.2", url="https://opensource.org/licenses/EUPL-1.2"
    ),
)

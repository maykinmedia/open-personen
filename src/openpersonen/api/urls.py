from django.conf import settings
from django.conf.urls import url
from django.urls import include

from vng_api_common import routers
from vng_api_common.schema import SchemaView as _SchemaView

from openpersonen.api.views.ingeschrevenpersoon import IngeschrevenPersoon
from openpersonen.api.schema import info

router = routers.DefaultRouter()

router.register(
    "ingeschrevenpersonen",
    IngeschrevenPersoon,
    base_name='ingeschrevenpersonen'
)


# set the path to schema file
class SchemaView(_SchemaView):
    # schema_path = settings.SPEC_URL["openpersonen"]
    info = info


urlpatterns = [
    # API documentation
    url(
        r"^schema/openapi(?P<format>\.json|\.yaml)$",
        SchemaView.without_ui(),
        name="schema-json-ingeschreven-persoon",
    ),
    url(
        r"^schema/$",
        SchemaView.with_ui(
            # "redoc"
        ),
        name="schema-redoc-ingeschreven-persoon",
    ),
    # actual API
    url(r"^", include(router.urls)),
]

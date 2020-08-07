from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers as drf_routers

from vng_api_common import routers
from vng_api_common.schema import SchemaView as _SchemaView

from openpersonen.api.views.ingeschrevenpersoon import IngeschrevenPersoon
from openpersonen.api.schema import info

router = routers.DefaultRouter()
router.register(r'ingeschrevenpersoon',
                IngeschrevenPersoon,
                base_name='ingeschrevenpersoon')

drf_routers = drf_routers.DefaultRouter()
drf_routers.register(r'ingeschrevenpersoon',
                     IngeschrevenPersoon,
                     base_name='ingeschrevenpersoon')


# set the path to schema file
class SchemaView(_SchemaView):
    info = info


urlpatterns = [
    # API documentation
    # url(
    #     r"^schema/openapi(?P<format>\.json|\.yaml)$",
    #     SchemaView(),
    #     name="schema-json-ingeschreven-persoon",
    # ),
    url(
        r"^schema/$",
        SchemaView.with_ui(
            # "redoc"
        ),
        name="schema-redoc-ingeschreven-persoon",
    ),

    # actual API
    path('', include(router.urls)),
    path('drf/', include(drf_routers.urls)),
]

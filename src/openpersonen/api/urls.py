from django.conf.urls import url
from django.urls import include, path

from vng_api_common import routers
from vng_api_common.schema import SchemaView as _SchemaView

from openpersonen.api.views import IngeschrevenPersoon, Kinder, Ouder, Partner
from openpersonen.api.schema import info

router = routers.DefaultRouter()

router.register(
    'ingeschrevenpersonen',
    IngeschrevenPersoon,
    base_name='ingeschrevenpersoon',
    nested=[
        routers.nested(
            'kinderen',
            Kinder,
            base_name='kinderen',
        ),
        routers.nested(
            'ouders',
            Ouder,
            base_name='ouders',
        ),
        routers.nested(
            'partners',
            Partner,
            base_name='partners',
        ),
    ]

)


# set the path to schema file
class SchemaView(_SchemaView):
    info = info


urlpatterns = [
    url(
        r"^schema/$",
        SchemaView.with_ui(
            # "redoc"
        ),
        name="schema-redoc-ingeschreven-persoon",
    ),

    # actual API
    path('', include(router.urls))
]

from django.conf.urls import url
from django.urls import include, path

from vng_api_common import routers
from vng_api_common.schema import SchemaView as _SchemaView

from openpersonen.api.views.ingeschrevenpersoon import IngeschrevenPersoon
from openpersonen.api.schema import info

router = routers.DefaultRouter()
router.register(r'ingeschrevenpersoon',
                IngeschrevenPersoon,
                base_name='ingeschrevenpersoon')


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

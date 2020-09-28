from django.conf.urls import url
from django.urls import include, path

from vng_api_common import routers
from vng_api_common.schema import SchemaView as _SchemaView

from openpersonen.api.schema import info
from openpersonen.api.views import (
    IngeschrevenPersoonViewSet,
    KindViewSet,
    NationaliteitHistorieViewSet,
    OuderViewSet,
    PartnerHistorieViewSet,
    PartnerViewSet,
    VerblijfPlaatsHistorieViewSet,
    VerblijfsTitelHistorieViewSet,
)

router = routers.DefaultRouter()


router.register(
    "ingeschrevenpersonen",
    IngeschrevenPersoonViewSet,
    base_name="ingeschrevenpersonen",
    nested=[
        routers.nested(
            "kinderen",
            KindViewSet,
            base_name="kinderen",
        ),
        routers.nested(
            "ouders",
            OuderViewSet,
            base_name="ouders",
        ),
        routers.nested(
            "partners",
            PartnerViewSet,
            base_name="partners",
        ),
        routers.nested(
            "verblijfplaatshistorie",
            VerblijfPlaatsHistorieViewSet,
            base_name="verblijfplaatshistorie",
        ),
        routers.nested(
            "partnerhistorie",
            PartnerHistorieViewSet,
            base_name="partnerhistorie",
        ),
        routers.nested(
            "verblijfstitelhistorie",
            VerblijfsTitelHistorieViewSet,
            base_name="verblijfstitelhistorie",
        ),
        routers.nested(
            "nationaliteithistorie",
            NationaliteitHistorieViewSet,
            base_name="nationaliteithistorie",
        ),
    ],
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
    path("", include(router.urls)),
]

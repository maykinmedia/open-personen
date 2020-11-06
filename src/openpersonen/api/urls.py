import os

from django.conf import settings
from django.conf.urls import url
from django.urls import include, path

from vng_api_common import routers
from vng_api_common.schema import SchemaView as _SchemaView

from openpersonen.api.schema import info
from openpersonen.api.views import (  # NationaliteitHistorieViewSet,; PartnerHistorieViewSet,; VerblijfPlaatsHistorieViewSet,; VerblijfsTitelHistorieViewSet,
    APIRootView,
    IngeschrevenPersoonViewSet,
    KindViewSet,
    OuderViewSet,
    PartnerViewSet,
)

router = routers.DefaultRouter()
router.APIRootView = APIRootView


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
        # routers.nested(
        #     "verblijfplaatshistorie",
        #     VerblijfPlaatsHistorieViewSet,
        #     base_name="verblijfplaatshistorie",
        # ),
        # routers.nested(
        #     "partnerhistorie",
        #     PartnerHistorieViewSet,
        #     base_name="partnerhistorie",
        # ),
        # routers.nested(
        #     "verblijfstitelhistorie",
        #     VerblijfsTitelHistorieViewSet,
        #     base_name="verblijfstitelhistorie",
        # ),
        # routers.nested(
        #     "nationaliteithistorie",
        #     NationaliteitHistorieViewSet,
        #     base_name="nationaliteithistorie",
        # ),
    ],
)


# set the path to schema file
class SchemaView(_SchemaView):
    schema_path = os.path.join(settings.BASE_DIR, "src", "openapi.yaml")
    info = info

    def get(self, request, version="", *args, **kwargs):
        if "format" in request.GET:
            #  The schema expects the format query param to be in the kwargs
            self.kwargs["format"] = request.GET["format"]

        return super().get(request, version=version, *args, **kwargs)


urlpatterns = [
    url(
        r"^schema/$",
        SchemaView.with_ui(
            # "redoc"
        ),
        name="schema-ingeschreven-persoon",
    ),
    # actual API
    path("", include(router.urls)),
]

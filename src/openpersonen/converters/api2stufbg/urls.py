from django.urls import path
from django.urls import include

from vng_api_common import routers

from .views import IngeschrevenPersoonViewSet, KindViewSet, OuderViewSet, PartnerViewSet


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
    ],
)


urlpatterns = [
    path("", include(router.urls)),
]

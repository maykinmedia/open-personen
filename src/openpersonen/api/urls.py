from django.conf.urls import url
from django.urls import include

from vng_api_common import routers

from openpersonen.api.views.ingeschrevenpersoon import IngeschrevenPersoon

router = routers.DefaultRouter()

router.register(
    "ingeschrevenpersonen",
    IngeschrevenPersoon,
    base_name='ingeschrevenpersonen'
)


urlpatterns = [
    url(r"^", include(router.urls)),
]

import os

from django.urls import include, path
from django.conf import settings
from django.conf.urls import url

from vng_api_common.schema import SchemaView as _SchemaView

from openpersonen.converters.schema import info


# set the path to schema file
class SchemaView(_SchemaView):
    schema_path = os.path.join(settings.BASE_DIR, "src", "openpersonen", "converters", "openapi.yaml")
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
    path(
        "api2stufbg/",
        include(
            ("openpersonen.converters.api2stufbg.urls", "openpersonen.converters"),
            namespace="api2stufbg",
        ),
    ),
    path(
        "stufbg2api/",
        include(
            ("openpersonen.converters.stufbg2api.urls", "openpersonen.converters"),
            namespace="stufbg2api",
        ),
    ),
]

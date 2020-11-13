from django.urls import include, path

urlpatterns = [
    path("api2stufbg/", include(("openpersonen.converters.api2stufbg.urls", "openpersonen.converters"), namespace='api2stufbg')),
    path("stufbg2api/", include(("openpersonen.converters.stufbg2api.urls", "openpersonen.converters"), namespace='stufbg2api')),
]

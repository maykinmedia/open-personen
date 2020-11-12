from django.urls import path

from openpersonen.converters.views import Api2StufbgView, Stufbg2ApiView

urlpatterns = [
    path("api2stufbg", Api2StufbgView.as_view(), name="api-2-stufbg"),
    path("stufbg2api", Stufbg2ApiView.as_view(), name="stufbg-2-api"),
]

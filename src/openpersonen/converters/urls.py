from django.urls import path

from openpersonen.converters.views import Stufbg2ApiView, Api2StufbgView

urlpatterns = [
    path("api2stufbg", Api2StufbgView.as_view(), name='api-2-stufbg'),
    path("stufbg2api", Stufbg2ApiView.as_view(), name='stufbg-2-api'),
]

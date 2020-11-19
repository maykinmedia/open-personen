from django.urls import path

from .views import KindView, OuderView, PartnerView, PersoonView

urlpatterns = [
    path(
        "ingeschrevenpersonen",
        PersoonView.as_view(),
        name="ingeschrevenpersonen-create",
    ),
    path("kinderen", KindView.as_view(), name="kinderen-create"),
    path("ouders", OuderView.as_view(), name="ouders-create"),
    path("partners", PartnerView.as_view(), name="partners-create"),
]

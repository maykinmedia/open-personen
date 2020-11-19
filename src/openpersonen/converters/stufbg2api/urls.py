from django.urls import path

from .views import KindView, OuderView, PartnerView, PersoonView

urlpatterns = [
    path(
        "ingeschrevenpersonen", PersoonView.as_view(), name="ingeschrevenpersonen-list"
    ),
    path("kinderen", KindView.as_view(), name="kinderen-list"),
    path("ouders", OuderView.as_view(), name="ouders-list"),
    path("partners", PartnerView.as_view(), name="partners-list"),
]

from django.urls import path

from .views import KindView, OuderView, PartnerView, PersoonView

urlpatterns = [
    path("ingeschrevenpersonen", PersoonView.as_view(), name="persoon"),
    path("kinderen", KindView.as_view(), name="kind"),
    path("ouders", OuderView.as_view(), name="ouder"),
    path("partners", PartnerView.as_view(), name="partner"),
]

from django.urls import path

from .views import PersoonView, KindView, OuderView, PartnerView

urlpatterns = [
    path("persoon", PersoonView.as_view(), name="persoon"),
    path("kind", KindView.as_view(), name="kind"),
    path("ouder", OuderView.as_view(), name="ouder"),
    path("partner", PartnerView.as_view(), name="partner"),
]

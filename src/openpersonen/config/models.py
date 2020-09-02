from django.db import models
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel


class StufBGConfig(SingletonModel):

    ontvanger_organisatie = models.CharField(max_length=200)
    ontvanger_administratie = models.CharField(max_length=200)
    ontvanger_applicatie = models.CharField(max_length=200)
    ontvanger_gebruiker = models.CharField(max_length=200)
    zender_organisatie = models.CharField(max_length=200)
    zender_administratie = models.CharField(max_length=200)
    zender_applicatie = models.CharField(max_length=200)
    zender_gebruiker = models.CharField(max_length=200)
    url = models.URLField(
        default="http://fieldlab.westeurope.cloudapp.azure.com:8081/brp/",
        help_text="URL to access Stuf-BG"
    )
    user = models.CharField(
        max_length=200, default="admin", help_text="Username for accessing Stuf-BG"
    )
    password = models.CharField(
        max_length=200, default="admin", help_text="Password for accessing Stuf-BG"
    )

    class Meta:
        verbose_name = _("Stuf BG Config")

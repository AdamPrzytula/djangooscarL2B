from django.db import models

from oscar.apps.address.abstract_models import AbstractAddress, AbstractUserAddress
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy
    


MR2, MISS2, MRS2 = ('Dev', 'Shop', 'Cars')
FRYTKI_CHOICES =(
    (MR2, _("Dev")),
    (MISS2, _("Shop")),
   	(MRS2, _("Cars")),
    )


class UserAddress(AbstractUserAddress):

    instaacc= models.CharField(_("Intagram Account"),max_length=255, blank=True)

    frytki=models.CharField(
        pgettext_lazy(u"Tak", u"frytki"),
        max_length=64, choices=FRYTKI_CHOICES, blank=True)


from oscar.apps.address.models import *
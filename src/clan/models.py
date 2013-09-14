from django.db import models

from utils.mixins import NewManualModelIdMixin


class Clan(models.Model, NewManualModelIdMixin):
    id = models.BigIntegerField(primary_key=True, null=False, blank=True)
    name = models.CharField(unique=True, max_length=25)
    description = models.CharField(max_length=1000)




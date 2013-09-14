from django.db import models

from utils.mixins import NewManualModelIdMixin

class Turn(models.Model, NewManualModelIdMixin):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)



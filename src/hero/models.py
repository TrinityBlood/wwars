# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _

from clan.models import Clan


class Hero(models.Model):
    class GENDER:
        MALE = u'male'
        FEMALE = u'female'
        ALL_DICT = {
            MALE: _(u'мужской'),
            FEMALE: _(u'женский')
        }
        ALL = ALL_DICT.items()

    name = models.CharField(max_length=30, blank=False, null=False)
    gender = models.CharField(max_length=10, choices=GENDER.ALL)
    created_at = models.DateTimeField(auto_now=True)
    icon = models.IntegerField(null=False)
    profile = models.OneToOneField(u'HeroProfile')
    clan = models.OneToOneField(Clan, name=u'clan')
    fleet=models.OneToOneField(u'Fleet', name=u'fleet')


class HeroProfile(models.Model):
    level = models.PositiveIntegerField(default=0)
    xp = models.BigIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    loses = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)

class Fleet(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)


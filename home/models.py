# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

# This code is triggered whenever a new user has been created and saved to the database


class TimeoutOption(models.Model):
    user_id = models.IntegerField(blank=False)
    timeout = models.IntegerField(blank=False)


class AccountNameOption(models.Model):
    user_id = models.IntegerField(blank=False)
    account_name = models.CharField(blank=False, max_length=100)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
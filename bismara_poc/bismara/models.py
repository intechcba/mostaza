from __future__ import unicode_literals

from django.db import models

DEFAULT_CHAR_VALUE = 'Unknown'

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100, null=False, default=DEFAULT_CHAR_VALUE)
    last_name = models.CharField(max_length=100, null=False, default=DEFAULT_CHAR_VALUE)
    address = models.CharField(max_length=200, null=False, default=DEFAULT_CHAR_VALUE)
    phone_number = models.CharField(max_length=20, null=False, default=DEFAULT_CHAR_VALUE)
    reg_number = models.CharField(max_length=20, null=False, default=DEFAULT_CHAR_VALUE)
    user = models.ForeignKey('auth.User', related_name='doctors', on_delete=models.CASCADE)


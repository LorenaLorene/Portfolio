from __future__ import unicode_literals

from django.db import models


class ContactPage(models.Model):
    page_name = models.CharField(max_length=200)
    contact_description = models.CharField(max_length=200)


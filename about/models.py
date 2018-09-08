from __future__ import unicode_literals

from django.db import models


class About(models.Model):
    page_name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    image = models.FileField(upload_to='assets/images')

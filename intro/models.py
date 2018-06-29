from __future__ import unicode_literals

from django.db import models


class Intro(models.Model):
    page_name = models.CharField(max_length=200)
    introduction = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    scroll_button = models.CharField(max_length=200)
    image = models.FileField(upload_to='assets/images')


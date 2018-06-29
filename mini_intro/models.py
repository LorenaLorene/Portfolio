from __future__ import unicode_literals

from django.db import models


class MiniIntro(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    image = models.FileField(upload_to='assets/images')

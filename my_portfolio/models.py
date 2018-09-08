from __future__ import unicode_literals

from django.db import models



class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    description_field = models.CharField(max_length=200)
    show = models.BooleanField(default=True)


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_link = models.CharField(max_length=200)
    image = models.FileField(upload_to='assets/images')

# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniIntro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='static/')),
            ],
        ),
    ]

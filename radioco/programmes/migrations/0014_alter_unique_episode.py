# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-22 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0013_programme_website'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together=set([]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_remove_project_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.CharField(default='error.html', max_length=85),
        ),
    ]

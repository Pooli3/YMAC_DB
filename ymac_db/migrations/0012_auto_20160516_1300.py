# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-05-16 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ymac_db', '0011_auto_20160516_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitedocument',
            name='filename',
            field=models.TextField(blank=True, null=True),
        ),
    ]

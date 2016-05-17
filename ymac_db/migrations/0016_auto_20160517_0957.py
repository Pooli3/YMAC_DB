# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-05-17 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ymac_db', '0015_auto_20160516_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitedocument',
            name='site',
        ),
        migrations.AlterField(
            model_name='sitedescriptions',
            name='site_description',
            field=models.CharField(
                choices=[('Artefacts / Scatter', 'Artefacts / Scatter'), ('Birthplace', 'Birthplace'),
                         ('Ceremonial', 'Ceremonial'), ('Engravings', 'Engravings'),
                         ('Grinding Patch', 'Grinding Patch'), ('Gnamma Hole', 'Gnamma Hole'),
                         ('Mythological', 'Mythological')], max_length=60),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0005_auto_20171019_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='transport_sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82'),
        ),
    ]

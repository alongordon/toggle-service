# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-25 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("inventit", "0004_auto_20190125_1446")]

    operations = [
        migrations.AddField(
            model_name="countheader",
            name="is_active",
            field=models.BooleanField(default=False),
        )
    ]

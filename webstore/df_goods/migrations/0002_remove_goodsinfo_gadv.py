# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gadv',
        ),
    ]
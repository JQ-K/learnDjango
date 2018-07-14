# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('df_user', '0002_auto_20180712_0434'),
        ('df_goods', '0003_auto_20180713_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo')),
            ],
        ),
    ]

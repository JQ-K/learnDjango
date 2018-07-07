# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField(db_column=b'pub_date')),
                ('bread', models.IntegerField()),
                ('bcomment', models.IntegerField()),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Hero_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.TextField()),
                ('isDelete', models.BooleanField()),
                ('book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_remove_userinfo_isdelete'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField(db_column=b'pub_date')),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField(default=True)),
                ('hcontent', models.TextField()),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]

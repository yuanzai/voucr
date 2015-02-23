# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc_url', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=255)),
                ('count', models.PositiveIntegerField()),
                ('expire_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('longname', models.CharField(max_length=255)),
                ('username_url', models.CharField(max_length=20, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_url', models.CharField(max_length=20, db_index=True)),
                ('word_url', models.CharField(max_length=20, db_index=True)),
                ('date_url', models.CharField(max_length=7, db_index=True)),
                ('expire_date', models.DateField()),
                ('campaign', models.ForeignKey(to='voucr.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaign',
            name='user',
            field=models.ForeignKey(to='voucr.UserInfo'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucr', '0008_voucher_is_claimed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address1',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='address2',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='country',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='zipcode',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
    ]

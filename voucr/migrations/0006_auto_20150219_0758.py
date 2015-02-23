# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucr', '0005_auto_20150219_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='img_path',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voucher',
            name='claim_datetime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucr', '0004_auto_20150219_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='expire_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]

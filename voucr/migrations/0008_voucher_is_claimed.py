# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucr', '0007_campaign_offer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='is_claimed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

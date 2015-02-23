# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucr', '0006_auto_20150219_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='offer_type',
            field=models.CharField(default=b'Free', max_length=30, choices=[(b'Free', b'Free'), (b'BuyNGet', b'Free With Purchase'), (b'Disc', b'Discount')]),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucr', '0002_remove_campaign_expire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='expire_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]

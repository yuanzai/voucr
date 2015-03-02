# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('voucr', '0010_auto_20150228_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default=b''),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucr', '0009_auto_20150226_0336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='address1',
            new_name='address_1',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='address2',
            new_name='address_2',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='longname',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='username_url',
            new_name='company_short_url',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='zipcode',
        ),
    ]

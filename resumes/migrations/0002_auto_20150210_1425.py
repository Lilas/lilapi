# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='resume',
        ),
        migrations.AddField(
            model_name='resume',
            name='mission',
            field=models.ManyToManyField(to='resumes.Mission'),
            preserve_default=True,
        ),
    ]

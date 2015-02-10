# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.IntegerField(default=50)),
                ('height', models.IntegerField(default=50)),
                ('readOnly', models.BooleanField(default=True)),
                ('fgColor', models.CharField(max_length=255, verbose_name=b'Color')),
                ('thickness', models.CharField(default=b'.2', max_length=255)),
                ('displayInput', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name of the skill')),
                ('data', models.CharField(max_length=255, verbose_name=b'Value of the skill')),
                ('option', models.ForeignKey(to='skills.Option')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

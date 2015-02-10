# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('more', jsonfield.fields.JSONField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('subname', models.CharField(max_length=255)),
                ('dateStart', models.CharField(max_length=32, verbose_name=b"D\xc3\xa9but de l'activit\xc3\xa9")),
                ('dateEnd', models.CharField(max_length=32, verbose_name=b"Fin de l'activit\xc3\xa9")),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResumeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Type de Resume',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='resume',
            name='resume_type',
            field=models.ForeignKey(to='resumes.ResumeType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='resume',
            field=models.ForeignKey(to='resumes.Resume'),
            preserve_default=True,
        ),
    ]

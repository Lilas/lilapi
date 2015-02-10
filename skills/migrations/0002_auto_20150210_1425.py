# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Type de Skill',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name': 'Options des Skill'},
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_type',
            field=models.ForeignKey(default=1, to='skills.SkillType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='option',
            name='fgColor',
            field=models.CharField(max_length=32, verbose_name=b'Color'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='option',
            name='thickness',
            field=models.CharField(default=b'.2', max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skill',
            name='data',
            field=models.CharField(max_length=3, verbose_name=b'Value of the skill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=32, verbose_name=b'Name of the skill'),
            preserve_default=True,
        ),
    ]

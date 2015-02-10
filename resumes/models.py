# -*- coding: utf-8 -*-

from django.db import models
from jsonfield import JSONField

from skills.models import Type


class Resume(models.Model):

    name = models.CharField(max_length=64)
    subname = models.CharField(max_length=255)
    dateStart = models.CharField(verbose_name="Début de l'activité",
                                 max_length=32)
    dateEnd = models.CharField(verbose_name="Fin de l'activité",
                               max_length=32)

    mission = models.ManyToManyField('resumes.Mission')

    resume_type = models.ForeignKey('resumes.ResumeType')

    def __unicode__(self):
        return self.name


class ResumeType(Type):

    class Meta:
        verbose_name = 'Type de Resume'


class Mission(models.Model):
    description = models.CharField(max_length=255)
    more = JSONField(blank=True)

    def __unicode__(self):
        return self.description

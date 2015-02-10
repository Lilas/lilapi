from django.db import models

class Type(models.Model):

    class Meta:
        abstract = True

    title = models.CharField(max_length=32)

    def __unicode__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(verbose_name="Name of the skill",
                            max_length=32)
    skill_type = models.ForeignKey('skills.SkillType')
    data = models.CharField(verbose_name="Value of the skill",
                            max_length=3)
    option = models.ForeignKey('skills.Option')

    def __unicode__(self):
        return self.name


class SkillType(Type):

    class Meta:
        verbose_name = 'Type de Skill'



class Option(models.Model):

    class Meta:
        verbose_name = 'Options des Skill'

    width = models.IntegerField(default=50)
    height = models.IntegerField(default=50)
    readOnly = models.BooleanField(default=True)
    fgColor = models.CharField(verbose_name="Color",
                               max_length=32)
    thickness = models.CharField(default=".2",
                                 max_length=3)
    displayInput = models.BooleanField(default=False)

    def __unicode__(self):
        return self.fgColor

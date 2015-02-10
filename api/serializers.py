# -*- coding: utf-8 -*-

from rest_framework import serializers

# /*
# **  SKILLS
# */
from skills.models import Skill
from skills.models import Option
from skills.models import SkillType

# /*
# **  RESUMES
# */
from resumes.models import Resume
from resumes.models import ResumeType
from resumes.models import Mission


class OptionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Option
        fields = ('width', 'height', 'readOnly',
                  'fgColor', 'thickness', 'displayInput', )


class SkillSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Skill
        fields = ('name', 'data', 'skill_type', 'option', )


class SkillTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SkillType
        fields = ('title',)


class ResumeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Resume
        fields = ('name', 'subname', 'dateStart', 'dateEnd', 'mission', 'resume_type', )


class ResumeTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ResumeType
        fields = ('title', )


class MissionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mission
        fields = ('description', 'more', )

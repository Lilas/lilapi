# -*- coding: utf-8 -*-

import django_filters

# /*
# **  SKILLS
# */
from skills.models import Skill

# /*
# **  RESUMES
# */
from resumes.models import Resume


class SkillFilter(django_filters.FilterSet):

    skill_type = django_filters.CharFilter(name="skill_type__title",
                                           lookup_type='icontains')

    class Meta:
        model = Skill
        fields = ['skill_type', ]


class ResumeFilter(django_filters.FilterSet):

    resume_type = django_filters.CharFilter(name="resume_type__title",
                                            lookup_type='icontains')

    class Meta:
        model = Resume
        fields = ['resume_type', ]

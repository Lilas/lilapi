# -*- coding: utf-8 -*-

from rest_framework import viewsets

# /*
# **  SKILLS
# */
from skills.models import Skill
from skills.models import Option
from skills.models import SkillType

from api.serializers import SkillSerializer
from api.serializers import OptionSerializer
from api.serializers import SkillTypeSerializer

# /*
# **  RESUMES
# */
from resumes.models import Resume
from resumes.models import ResumeType
from resumes.models import Mission

from api.serializers import ResumeSerializer
from api.serializers import MissionSerializer
from api.serializers import ResumeTypeSerializer

from api import filters


class SkillViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows skill to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_class = filters.SkillFilter


class OptionViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows option to be viewed or edited.
    """
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class SkillTypeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows skill_type to be viewed or edited.
    """
    queryset = SkillType.objects.all()
    serializer_class = SkillTypeSerializer


class ResumeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows resume to be viewed or edited.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeTypeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows resume_type to be viewed or edited.
    """
    queryset = ResumeType.objects.all()
    serializer_class = ResumeTypeSerializer


class MissionViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows mission to be viewed or edited.
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    filter_class = filters.ResumeFilter

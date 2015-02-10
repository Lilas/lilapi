# -*- coding: utf-8 -*-

from django.contrib import admin

from skills.models import Skill
from skills.models import SkillType
from skills.models import Option

admin.site.register(Skill)
admin.site.register(Option)
admin.site.register(SkillType)

# -*- coding: utf-8 -*-

from django.contrib import admin

from resumes.models import Resume
from resumes.models import ResumeType
from resumes.models import Mission

admin.site.register(Resume)
admin.site.register(ResumeType)
admin.site.register(Mission)
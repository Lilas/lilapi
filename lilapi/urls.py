from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet)
router.register(r'options', views.OptionViewSet)
router.register(r'skill_type', views.SkillTypeViewSet)
router.register(r'resumes', views.ResumeViewSet)
router.register(r'resume_type', views.ResumeTypeViewSet)
router.register(r'missions', views.MissionViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

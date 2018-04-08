from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),

    #url for module control
    url(r'^module-control/$', views.ModuleControl.as_view(), name='module-control'),

    #url for lesson control
    url(r'^lesson-control/$', views.LessonControl.as_view(), name='lesson-control'),
    url(r'^lesson-detail/(?P<module_id>[0-9]+)/$', views.LessonDetail.as_view(), name='lesson-detail'),

    #url for step control
    url(r'^step-control/$', views.StepControls.as_view(), name='step-control'),

    #url for control affiliate link
    url(r'^affiliate-link-control/$', views.AffiliateLinkControls.as_view(), name='affiliate-link-control'),

    #add video on lesson
    url(r'^video/add/$', views.AddVideo.as_view(), name='add-video'),

]

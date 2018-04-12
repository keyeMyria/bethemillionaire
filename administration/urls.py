from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),

    #user management
    url(r'^user/all/$', views.AllUser.as_view(), name='all-user'),
    url(r'^user/detail/(?P<user_id>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^user/(?P<user_id>[0-9]+)/edit/$', views.EditUser.as_view(), name='edit-user'),
    url(r'^user/(?P<user_id>[0-9]+)/change-password/$', views.ChangeUserPassword.as_view(), name='change-user-password'),
    url(r'^user/(?P<profile_status>[a-zA-z]+)/(?P<user_id>[0-9]+)/$', views.ActiveDeactiveUser.as_view(), name='active-deactive-user'),
    url(r'^user/(?P<user_id>[0-9]+)/delete/$', views.DeleteUser.as_view(), name='delete-user'),


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

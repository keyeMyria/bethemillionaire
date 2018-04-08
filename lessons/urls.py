from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^module-1/$', views.Module1.as_view(), name='module_1'),
    url(r'^module-2/$', views.Module2.as_view(), name='module_2'),
    url(r'^module-3/$', views.Module3.as_view(), name='module_3'),
    url(r'^module-4/$', views.Module4.as_view(), name='module_4'),
    url(r'^module-5/$', views.Module5.as_view(), name='module_5'),
    url(r'^module-6/$', views.Module6.as_view(), name='module_6'),
    url(r'^module-7/$', views.Module7.as_view(), name='module_7'),
]

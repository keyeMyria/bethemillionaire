from django.conf.urls import url
from . import views


urlpatterns = [
    #dashboard - bitcoin basics links
    url(r'^how-to-grow-your-wealth-in-bitcoins/$', views.Course.as_view(), name='course'),
]

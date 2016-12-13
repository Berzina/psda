from django.conf.urls import url, include
from . import views

urlpatterns = [
      url(r'^$', views.scenarios, name='scenarios'),
      url(r'^room/(?P<room_type_id>[0-9]+)/(?P<roomobject_id>[0-9]+)$', views.room, name='room'),
      url(r'^devices$', views.devices, name='devices'),
      url(r'^satisfy$', views.satisfy, name='satisfy'),
      url(r'^ajaxrequest$', views.ajax_catcher, name='ajax_catcher')]
from django.conf.urls import url, include
from . import views

urlpatterns = [
      url(r'^$', views.scenarios, name='scenarios'),
      url(r'^room/(?P<room_id>[0-9]+)$', views.room, name='room'),
      url(r'^devices$', views.devices, name='devices')]
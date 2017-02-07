from django.conf.urls import url, include
from . import views
from django.views.generic.base import RedirectView
from  django.contrib.auth.views import login
from django.contrib import admin

urlpatterns = [
      url(r'^$', views.home, name='home'),
      url(r'^login$', views.login, name='login'),
      url(r'^room/(?P<room_type_id>[0-9]+)/(?P<roomobject_id>[0-9]+)$', views.room, name='room'),
      url(r'^devices$', views.devices, name='devices'),
      url(r'^device_state$', views.get_device_state, name='device_state'),
      url(r'^scenario_state$', views.get_scenario_state, name='scenario_state'),
      url(r'^charts$', views.charts, name='charts'),
      url(r'^satisfy$', views.satisfy, name='satisfy'),
      url(r'^redraw_charts$', views.redraw_charts, name='redraw_charts'),
      url(r'^ajaxrequest$', views.ajax_catcher, name='ajax_catcher'),
      url(r'^ajaxresponse$', views.ajax_responser, name='ajax_responser'),
      url(r'^token_validator$', views.token_validator, name='token_validator'),
      url(r'^toggle_device$', views.toggle_device, name='toggle_device'),
      url(r'^toggle_scenario$', views.toggle_scenario, name='toggle_scenario'),
      url(r'^logout$', views.logout, name='logout'),
      url(r'^admin/', RedirectView.as_view(url='/admin'), name='admin')]

admin.site.site_header = 'EZhome administration'
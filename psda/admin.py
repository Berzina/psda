from django.contrib import admin

from .models import Device, DeviceList, RoomList, Rooms, Members, Events, Scenarios

admin.site.register(Device)
admin.site.register(DeviceList)
admin.site.register(RoomList)
admin.site.register(Rooms)
admin.site.register(Members)
admin.site.register(Events)
admin.site.register(Scenarios)

from django.shortcuts import render, get_object_or_404
from .models import Device, DeviceList, Rooms, Scenarios, RoomList, Events
from django_ajax.decorators import ajax

def index(request):

    device_list = DeviceList.objects.all()
    room_list = RoomList.objects.all()
    context = {"devices" : device_list,
               "current_roomtype" : "overview",
               "rooms" : room_list}

    return render(request, 'psda/index.html', context)

def room(request, room_type_id, roomobject_id):

    room_type = RoomList.objects.get(pk=room_type_id)
    room_list = RoomList.objects.all()

    context = {"current_roomtype" : room_type,
               "rooms": room_list,
               "room_id" : roomobject_id,
               "room_object" : Rooms.objects.get(pk=roomobject_id)}

    return render(request, 'psda/roomview.html', context)

def scenarios (request):
    scenario_list = Scenarios.objects.all()
    room_list = RoomList.objects.all()
    events = Events.objects.all()
    context = {"scenarios" : scenario_list,
               "current_roomtype" : "overview",
               "tab" : "scenarios",
               "rooms": room_list,
               "events" : events}

    return render(request, 'psda/index.html', context)

def devices (request):
    device_list = DeviceList.objects.all()
    room_list = RoomList.objects.all()
    context = {"devices" : device_list,
               "current_roomtype" : "overview",
               "tab" : "devices",
               "rooms": room_list}

    return render(request, 'psda/index.html', context)
@ajax
def satisfy (request):
    return {'result':'i love u kate, u are very cute and smart person :3'}
from django.shortcuts import render, get_object_or_404
from .models import Device, DeviceList, Rooms, Scenarios
from django_ajax.decorators import ajax

def index(request):

    device_list = DeviceList.objects.all()
    context = {"devices" : device_list,
               "room" : "overview"}

    return render(request, 'psda/index.html', context)

def room(request, room_id):

    room = Rooms.objects.get(pk=room_id)
    device_list = room.device_set.all()
    context = {"devices" : device_list,
               "room" : room}

    return render(request, 'psda/roomview.html', context)

def scenarios (request):
    scenario_list = Scenarios.objects.all()
    context = {"scenarios" : scenario_list,
               "room" : "overview",
               "tab" : "scenarios"}

    return render(request, 'psda/index.html', context)

def devices (request):
    device_list = DeviceList.objects.all()
    context = {"devices" : device_list,
               "room" : "overview",
               "tab" : "devices"}

    return render(request, 'psda/index.html', context)
@ajax
def satisfy (request):
    return {'result':'i love u kate, u are very cute and smart person :3'}
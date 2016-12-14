from django.shortcuts import render, get_object_or_404
from .models import Device, DeviceList, Rooms, Scenarios, RoomList, Events, AjaxRequests
from django_ajax.decorators import ajax
from django.views.decorators.csrf import csrf_exempt


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
    room_object = Rooms.objects.get(pk=roomobject_id)
    devices = room_object.device_set.all()


    context = {"current_roomtype" : room_type,
               "rooms": room_list,
               "room_id" : roomobject_id,
               "room_object" : room_object,
               "devices" : devices}



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

@ajax
@csrf_exempt
def ajax_catcher (request):

    print ("I got ajax request!")

    device_values = {}

    for param, value in request.POST.items():

### -------- Required fields ------- ###
        if param == "token":
            token = value
        if param == "request_type":
            request_type = value
        if param == "device":
            device = value
        if param == "state":
            state = value
### --------------------------------- ###

        if param == "value1":
            device_values ["value1"] = value
        if param == "value2":
            device_values["value2"] = value
        if param == "value3":
            device_values["value3"] = value
        if param == "value4":
            device_values["value4"] = value
        if param == "value5":
            device_values["value5"] = value



    request_template = AjaxRequests.objects.get(pk=1)

    if token and token == request_template.token:
        good_token = True
    if request_type and device and state:
        good_params = True

    proper_request = good_token and good_params

    if proper_request:
        return {'success':
                    {'device_id': str(device), 'state_id': str(state), 'device_values': device_values}}
    else:
        return {'error': 'Incorrect request', 'params': [token, device, state, device_values]}

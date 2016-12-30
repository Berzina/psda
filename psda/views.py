from django.shortcuts import render, get_object_or_404, redirect
from .models import Device, DeviceList, Rooms, Scenarios, RoomList, Events, AjaxRequests, Commands, CommandList, StatusList, Statistics
from django_ajax.decorators import ajax
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import os
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.template.loader import render_to_string


def login (request):

  print (request.POST)
  username = request.POST.get("username", False)
  password = request.POST.get("password", False)
  try:
      user = authenticate(username=username, password=password)
      login_django(request, user)
      # Always return an HttpResponseRedirect after successfully dealing
      # with POST data. This prevents data from being posted twice if a
      # user hits the Back button.
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  except:
      return HttpResponseRedirect('/')




def index(request):

    context = {"current_roomtype" : "overview",
               "tab": "scenarios"}

    return render(request, 'psda/index.html', context)

def room(request, room_type_id, roomobject_id):

    room_type = RoomList.objects.get(pk=room_type_id)
    room_list = RoomList.objects.all()
    try:
        room_object = Rooms.objects.get(pk=roomobject_id)
        devices = room_object.device_set.all()
        context = {"current_roomtype" : room_type,
                   "rooms": room_list,
                   "room_id" : roomobject_id,
                   "room_object" : room_object,
                   "devices" : devices,
                   "tab" : "room"}
        return render(request, 'psda/roomview.html', context)
    except:
        context = {"current_roomtype": room_type,
                   "rooms": room_list,
                   "tab": "room"}
        return render(request, 'psda/noroomview.html', context)

def scenarios (request):
    t= timezone.now()
    print ("start")
    scenario_list = Scenarios.objects.all()
    print (scenario_list.values())

    t1 = timezone.now() - t
    print ("scena loaded : ", t1)
    room_list = RoomList.objects.all()

    t2 = timezone.now() - t - t1
    print ("events loaded : ", t2)

    t3 = timezone.now()
    print ("making computes...")
    scenarios = {}

    for scenario in scenario_list:
        past_events = {}
        future_events = {}
        events = scenario.events_set.all()

        for event in events:
            if scenario.id == event.scenario_id:
                if event.event_type.id == 1:
                    past_events[event.device.name] = event.command.description
                if event.event_type.id == 2:
                    future_events[event.device.name] = event.command.description

        scenarios [scenario.id] = {"name" : scenario.name, "descr": scenario.description, "state" : scenario.state.name,
                                   "events" : {
                                       "past" : past_events,
                                       "future" : future_events
                                   }}

    t4 = timezone.now() - t3
    print ("computed:", t4)
    context = {"scenarios" : scenarios,
               "current_roomtype" : "overview",
               "tab" : "scenarios",
               "rooms": room_list}

    t5 = timezone.now()
    print ("start rendering")
    ret = render(request, 'psda/index.html', context)
    t6 = timezone.now() - t5
    print ("rendered : ", t6)
    print ("score: ", timezone.now() - t)
    return ret

def devices (request):
    t= timezone.now()
    print ("start")
    device_list = Device.objects.all()
    t1 = timezone.now() - t
    print ("device loaded : ", t1)
    room_list = RoomList.objects.all()
    t2 = timezone.now() - t - t1
    print ("rooms loaded : ", t2)
    context = {"devices" : device_list,
               "current_roomtype" : "overview",
               "tab" : "devices",
               "rooms": room_list}
    t3 = timezone.now()
    print ("start rendering")
    ret = render(request, 'psda/index.html', context)
    t4 = timezone.now() - t3
    print ("rendered : ", t4)
    return ret

def charts (request):
    room_list = RoomList.objects.all()

    devices = Device.objects.all().filter(collect_statistic=1)
    statistics = Statistics.objects.all()
    stats = []
    today = timezone.now()
    for stat in statistics:
        if stat.date_time.month == today.month and stat.date_time.day == today.day:
            stats.append(stat)

    date = str(today.year) + "-" + str(today.month) + "-" + str(today.day)

    print (date)

    context = {"devices": devices,
               "current_roomtype" : "overview",
               "tab" : "charts",
               "rooms": room_list,
               "statistics": stats,
               "date": date}

    return render(request, 'psda/index.html', context)
@ajax
def satisfy (request):
    return {'result':'i love u kate, u are very cute and smart person :3'}

@ajax
@csrf_exempt
def toggle_device (request):

    device_id = int(request.POST["device"])
    state_id = int(request.POST["state"])

    device = Device.objects.get(pk=device_id)
    scenario = Scenarios.objects.get(name="NONE")

    if state_id == 3:
        command = CommandList.objects.get(name="TURN_OFF")
        state= StatusList.objects.get(name="WAIT")
        Commands.objects.create(device=device, scenario=scenario, command=command, state=state, date_time=timezone.now(), value=0)
    elif state_id == 5:
        command = CommandList.objects.get(name="TURN_ON")
        print (command.id)
        state= StatusList.objects.get(name="WAIT")
        Commands.objects.create(device=device, scenario=scenario, command=command, state=state,
                                date_time=timezone.now(), value=0)
    return {'result': request.POST["device"] + " " + request.POST["state"]}

@ajax
@csrf_exempt
def toggle_scenario (request):

    scenario_id = int(request.POST["scenario"])
    state_id = int(request.POST["state"])

    device = Device.objects.get(name="NONE")
    scenario = Scenarios.objects.get(pk=scenario_id)

    if state_id == 3:
        command = CommandList.objects.get(name="STOP_SCEN")
        state= StatusList.objects.get(name="WAIT")
        Commands.objects.create(device=device, scenario=scenario, command=command, state=state, date_time=timezone.now(), value=0)
    elif state_id == 5:
        command = CommandList.objects.get(name="RUN_SCEN")
        state= StatusList.objects.get(name="WAIT")
        Commands.objects.create(device=device, scenario=scenario, command=command, state=state,
                                date_time=timezone.now(), value=0)
    return {'result': request.POST["scenario"] + " " + request.POST["state"]}

@ajax
@csrf_exempt
def token_validator (request):

    request_template = AjaxRequests.objects.get(pk=1)
    if (request.POST["token"] == request_template.token):
        return {'valid': 'ok'}
    else:
        return {'valid': 'false'}


@ajax
@csrf_exempt
def redraw_charts(request):
    date_str = request.POST["date"]
    date_list = date_str.split("-") #[yyyy, mm, dd]

    devices = Device.objects.all().filter(collect_statistic=1)
    statistics = Statistics.objects.all()
    stats = []

    for stat in statistics:
        if stat.date_time.month == int(date_list[1]) and stat.date_time.day == int(date_list[2]):
            stats.append(stat)

    context = {'devices': devices,
               'statistics': stats}

    content = render_to_string('psda/includes/chartlist.html', context)

    return {'html': content}

@ajax
@csrf_exempt
def ajax_catcher (request):

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

        print (param, value)

    request_template = AjaxRequests.objects.get(pk=1)

    print (request.path)

    if token and token == request_template.token:
        good_token = True
    if request_type and device and state:
        good_params = True

    proper_request = good_token and good_params

    redirect('ajax_responser')


    if proper_request:
        return {'success':
                    {'device_id': str(device), 'state_id': str(state), 'device_values': device_values}}
    else:
        return {'error': 'Incorrect request', 'params': [token, device, state, device_values]}


@ajax
@csrf_exempt
def ajax_responser(request):
    return {'success': 'ok'}


def logout(request):
    logout_django(request)
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect("/")

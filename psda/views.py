from django.shortcuts import render, get_object_or_404
from .models import Device, DeviceList


def index(request):

    device_list = DeviceList.objects.all()
    context = {"devices" : device_list}

    return render(request, 'psda/index.html', context)
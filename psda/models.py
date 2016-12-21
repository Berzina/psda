from __future__ import unicode_literals

from django.db import models

class AjaxRequests(models.Model):
    id = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=20)
    request_type = models.CharField(max_length=5)
    device = models.IntegerField()
    state = models.IntegerField()
    value = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ajax_requests'

class ChannelList(models.Model):
    name = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'channel_list'


class CommandList(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'command_list'


class Commands(models.Model):
    device = models.ForeignKey('Device', models.DO_NOTHING, db_column='device')
    scenario = models.ForeignKey('Scenarios', models.DO_NOTHING, db_column='scenario')
    command = models.ForeignKey(CommandList, models.DO_NOTHING, db_column='command')
    value = models.FloatField()
    state = models.ForeignKey('StatusList', models.DO_NOTHING, db_column='state')
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'commands'


class Device(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)
    card_color = models.CharField(max_length=20)
    state = models.ForeignKey('StatusList', models.DO_NOTHING, db_column='state')
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room')
    channel = models.ForeignKey(ChannelList, models.DO_NOTHING, db_column='channel')
    type = models.ForeignKey('DeviceList', models.DO_NOTHING, db_column='type')
    voltage = models.FloatField()
    logic = models.IntegerField()
    collect_statistic = models.IntegerField()
    pin1 = models.IntegerField()
    pin2 = models.IntegerField()
    pin3 = models.IntegerField()
    pin4 = models.IntegerField()
    pin5 = models.IntegerField()
    pin6 = models.IntegerField()
    pin7 = models.IntegerField()
    pin8 = models.IntegerField()
    pin9 = models.IntegerField()
    pin10 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'device'

    def __str__(self):
        return self.name


class DeviceList(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'device_list'

    def __str__(self):
        return self.name

class EventList(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'event_list'


class Events(models.Model):
    scenario = models.ForeignKey('Scenarios', models.DO_NOTHING, db_column='scenario')
    event_type = models.ForeignKey(EventList, models.DO_NOTHING, db_column='event_type')
    device = models.ForeignKey(Device, models.DO_NOTHING, db_column='device')
    run_scena = models.IntegerField()
    command = models.ForeignKey(CommandList, models.DO_NOTHING, db_column='command')
    value1 = models.FloatField()
    value2 = models.FloatField()
    value3 = models.FloatField()
    value4 = models.FloatField()
    member = models.ForeignKey('Members', models.DO_NOTHING, db_column='member')

    class Meta:
        managed = False
        db_table = 'events'

    def __str__(self):
        return self.name


class Members(models.Model):
    name = models.CharField(max_length=20)
    v1 = models.IntegerField()
    v2 = models.IntegerField()
    v3 = models.IntegerField()
    v4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'members'

    def __str__(self):
        return self.name


class RoomList(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'room_list'

    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=20)
    type_room = models.ForeignKey(RoomList, models.DO_NOTHING, db_column='type_room')

    class Meta:
        managed = False
        db_table = 'rooms'

    def __str__(self):
        return self.name


class Scenarios(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    state = models.ForeignKey('StatusList', models.DO_NOTHING, db_column='state')
    auto = models.IntegerField()
    date_create = models.DateTimeField()
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    days_of_week = models.IntegerField()
    time_of_daye_begin = models.TimeField()
    time_of_daye_end = models.TimeField()
    period_sec = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scenarios'

    def __str__(self):
        return self.name


class Statistics(models.Model):
    date_time = models.DateTimeField()
    device = models.ForeignKey(Device, models.DO_NOTHING, db_column='device')
    value1 = models.FloatField()
    value2 = models.FloatField()
    value3 = models.FloatField()
    value4 = models.FloatField()
    value5 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'statistics'


class StatusList(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'status_list'


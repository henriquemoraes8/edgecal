from django.db import models
from django_enumfield import enum
from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User

##############
# Enumerations
##############

class Weekday(enum.Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    
class AccessLevel(enum.Enum):
    PRIVATE = 0
    BUSY = 1
    VISIBLE = 2
    MODIFY = 3
    
##############
# Database Entities
##############

class CalendarUser(models.Model):
    # TODO: Add any additional attributes for users
    user = models.OneToOneField(User)

class Event(models.Model):
    creator = models.ForeignKey(CalendarUser, related_name='creator') # M Events --> 1 Creator
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=40, blank = True)
    event_description = models.CharField(max_length=140, blank = True)
    notes = models.CharField(max_length=500, blank = True)
    repetition_end_date = models.DateField() 
    public_access_level = enum.EnumField(AccessLevel, default = AccessLevel.PRIVATE)

    members = models.ManyToManyField(CalendarUser, through='IsAttending', through_fields=('event', 'user'))
    #repetition_scheme = models.ManyToManyField(Weekday, through='EventRepeatsOn', through_fields=('event', 'weekday'))

    # TODO: Make notes its own class?

    def __str__(self):
        return self.commitment_description
    
class IsAttending(models.Model):
    user = models.ForeignKey(CalendarUser)
    event = models.ForeignKey(Event)
    
#class EventRepeatsOn(models.Model):
#    event = models.ForeignKey(Event)
#    weekday = models.ForeignKey(Weekday)

class HasAccess(models.Model):
    user = models.ForeignKey(CalendarUser)
    event = models.ForeignKey(Event)
    visibility = enum.EnumField(AccessLevel, default = AccessLevel.PRIVATE)

class Rule(models.Model):
    priority = models.IntegerField(default = 0)
    status = enum.EnumField(AccessLevel, default = AccessLevel.PRIVATE)

class Alert(models.Model):
    alert_date = models.DateField()
    event = models.ForeignKey(Event)

    def send_mail(self):
        pass
    def notify_on_application(self):
        pass

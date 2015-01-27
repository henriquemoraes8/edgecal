from django.db import models
from django_enumfield import enum
from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User

class CalendarUser(models.Model):
    # TODO: Add any additional attributes for users
    user = models.OneToOneField(User)

class Event(models.Model):
    creator = models.ForeignKey(CalendarUser) # M Events --> 1 Creator
    event_date = models.DateField()
    location = models.CharField(max_length=40, blank = True)
    event_description = models.CharField(max_length=100, blank = True)
    #visibility = models.OneToOneField(Visibility);
    # repetition = something

    def __str__(self):
        return self.commitment_description
    
class IsAttending(models.Model):
    user = models.ForeignKey(CalendarUser)
    event = models.ForeignKey(Event)

class VisibilityStatus(enum.Enum):
    PRIVATE = 0
    BUSY = 1
    VISIBLE = 2
    MODIFY = 3

class Rule(models.Model):
    priority = models.IntegerField(default = 0)
    # visibility = models.ForeignKey(Visibility)
    status = enum.EnumField(VisibilityStatus, default = VisibilityStatus.PRIVATE)

class Alert(models.Model):
    alert_date = models.DateField()
    event = models.ForeignKey(Event)

    def send_mail(self):
        pass
    def notify_on_application(self):
        pass

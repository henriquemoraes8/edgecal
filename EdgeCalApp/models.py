from django.db import models
from django_enumfield import enum
from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from codetools.util.cbook import Null

##############
# Enumerations
##############

class WeekdayEnum(enum.Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    
class Weekday(models.Model):
    day = enum.EnumField(WeekdayEnum, default = Null)
    
class AccessLevel(enum.Enum):
    PRIVATE = 0
    BUSY = 1
    VISIBLE = 2
    MODIFY = 3

class InvitationStatus(enum.Enum):
    AWAITING_RESPONSE = 0
    DECLINED = 1
    MAYBE = 2
    ATTENDING = 3


##############
# Database Entities
##############

class CalendarUser(models.Model):    
    user = models.OneToOneField(User)
    
    users = models.Manager()
    
    # TODO: Add any additional attributes for users
    
    def save(self, *args, **kwargs):
        # do_something()
        super(CalendarUser, self).save(*args, **kwargs) # Call the "real" save() method.
        # do_something_else()
    
    def __str__(self):
        return self.commitment_description

# Design Note: Should we rename this something like 'Entry' ?  What if we want to add
# more general 'tasks' later? I feel like a lot of this could be recycled...

class Event(models.Model):
    creator = models.ForeignKey(CalendarUser, related_name='Creator') # M Events --> 1 Creator
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    location = models.CharField(max_length=40, blank = True)
    description = models.CharField(max_length=140, blank = True)
    notes = models.CharField(max_length=500, blank = True)
    end_repeat_date = models.DateField() 
    public_access_level = enum.EnumField(AccessLevel, default = AccessLevel.PRIVATE)

    guest_list = models.ManyToManyField(CalendarUser, through='IsInvited', through_fields=('event', 'user'))
    repetition_scheme = models.ManyToManyField(Weekday)
    
    events = models.Manager()
    
    class Meta:
        ordering = ["start_date_time"]
        verbose_name_plural = "Events"

    # TODO: Specify widgets to be used for each field
    # TODO: Make notes its own class?

    def save(self, *args, **kwargs):
        # do_something()
        super(Event, self).save(*args, **kwargs) # Call the "real" save() method.
        # do_something_else()

    def __str__(self):
        return self.commitment_description
    
class IsInvited(models.Model):
    user = models.ForeignKey(CalendarUser)
    event = models.ForeignKey(Event)
    invitation_status = enum.EnumField(InvitationStatus, default = InvitationStatus.AWAITING_RESPONSE)
    # invited_by = models.ForeignKey(CalendarUser)
    
    # TODO: Add specific invitation message ?
    
    def __str__(self):
        return self.commitment_description

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

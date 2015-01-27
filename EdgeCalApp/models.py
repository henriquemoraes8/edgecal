from django.db import models
from django_enumfield import enum
from annoying.fields import AutoOneToOneField

class Calendar(models.Model):
    def mode_day(self):
        pass
    def mode_week(self):
        pass
    def mode_month(self):
        pass

class Visibility(models.Model):
    def get_rule_for_user(self, user):
        pass
    def get_rule_for_group(self, group):
        pass

class Event(models.Model):
    event_date = models.DateField()
    calendar = models.ForeignKey(Calendar)
    location = models.CharField(max_length=40, blank = True)
    event_description = models.CharField(max_length=100, blank = True)
    visibility = models.OneToOneField(Visibility);

    def __str__(self):
        return self.commitment_description

class VisibilityStatus(enum.Enum):
    PRIVATE = 0
    BUSY = 1
    VISIBLE = 2
    MODIFY = 3

class Rule(models.Model):
    priority = models.IntegerField(default = 0)
    visibility = models.ForeignKey(Visibility)
    status = enum.EnumField(VisibilityStatus, default = VisibilityStatus.PRIVATE)

class Alert(models.Model):
    alert_date = models.DateField()
    event = models.ForeignKey(Event)

    def send_mail(self):
        pass
    def notify_on_application(self):
        pass

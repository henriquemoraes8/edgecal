from django.contrib import admin

from EdgeCalApp.models import CalendarUser, Event, Rule, Alert

admin.site.register(CalendarUser)
admin.site.register(Event)
admin.site.register(Rule)
admin.site.register(Alert)

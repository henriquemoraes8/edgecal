from django.contrib import admin

from EdgeCalApp.models import Calendar, Visibility, Event, Rule, Alert

admin.site.register(Calendar)
admin.site.register(Visibility)
admin.site.register(Event)
admin.site.register(Rule)
admin.site.register(Alert)

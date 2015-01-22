from django.contrib import admin

from EdgeCalApp.models import User, Calendar, Visibility, Event, Rule, Alert

admin.site.register(User)
admin.site.register(Calendar)
admin.site.register(Visibility)
admin.site.register(Event)
admin.site.register(Rule)
admin.site.register(Alert)

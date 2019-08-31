import xadmin
from Activity.models import Event
# Register your models here.


class EventAdmin(object):
    list_display = ['id', 'state', 'type', 'event_title', 'event_alt', 'url', 'img', 'begin_date', 'end_date']
    search_fields = ['event_title', 'event_alt', 'event_body', 'url']
    list_filter = ['state', 'type', 'operator']
    list_editable = ['state']
    style_fields = {"event_body": "ueditor"}


xadmin.site.register(Event, EventAdmin)

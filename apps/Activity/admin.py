import xadmin
from Activity.models import Event, Receive, Crowdfunding, QQGroup, Topic
# Register your models here.


class EventAdmin(object):
    list_display = ['id', 'state', 'type', 'event_title', 'event_alt', 'url', 'img', 'begin_date', 'end_date']
    search_fields = ['event_title', 'event_alt', 'event_body', 'url']
    list_filter = ['state', 'type', 'operator']
    list_editable = ['state']
    style_fields = {"event_body": "ueditor"}


class ReceiveAdmin(object):
    list_display = ['id', 'event_code', 'qq', 'description', 'date']
    search_fields = ['qq', 'description']
    list_filter = ['event_code', 'qq', 'date']


class CrowdfundingAdmin(object):
    list_display = ['id', 'event_code', 'qq', 'name', 'point', 'description', 'date']
    search_fields = ['qq', 'description']
    list_filter = ['event_code', 'qq', 'date']


class QQGroupAdmin(object):
    list_display = ['name', 'num', 'state', 'description']
    search_fields = ['num']
    list_filter = ['state']


class TopicAdmin(object):
    list_display = ['topic', 'type', 'state', 'create_time', 'point', 'description']
    search_fields = ['topic']
    list_editable = ['state', 'point']
    list_filter = ['type', 'state']


xadmin.site.register(Event, EventAdmin)
xadmin.site.register(Receive, ReceiveAdmin)
xadmin.site.register(Crowdfunding, CrowdfundingAdmin)
xadmin.site.register(QQGroup, QQGroupAdmin)
xadmin.site.register(Topic, TopicAdmin)

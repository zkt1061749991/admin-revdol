import xadmin
from MessageCenter.models import FeedBack, Notice


class FeedBackAdmin(object):
    list_display = ['id', 'qq', 'feedback_state', 'feedback_type', 'feedback_body', 'feedback_date']
    search_fields = ['qq', 'feedback_body']
    list_filter = ['feedback_type', 'feedback_date']
    readonly_fields = ['qq', 'feedback_body', 'feedback_date']
    list_editable = ['feedback_state']


class NoticeAdmin(object):
    list_display = ['id', 'notice_title', 'notice_date', 'operator']
    search_fields = ['notice_title', 'notice_body']
    list_filter = ['notice_date', 'operator']
    style_fields = {"notice_body": "ueditor"}


xadmin.site.register(FeedBack, FeedBackAdmin)
xadmin.site.register(Notice, NoticeAdmin)

import xadmin
from PlatForm.models import PointLog, Prize, Order, Forum


class PointLogAdmin(object):
    list_display = ['operated_qq', 'state', 'type', 'operate_type', 'operate_point', 'description', 'forum_id', 'operator', 'operate_date']
    search_fields = ['description', 'operated_qq__qq', 'forum_id']
    list_filter = ['state', 'type', 'operate_type', 'operate_point', 'operate_date']
    show_detail_fields = ['operated_qq']
    list_editable = ['state', 'operate_point', 'description']
    readonly_fields = ['forum_id', 'explain']


class PrizeAdmin(object):
    list_display = ['id', 'prize_no', 'publish', 'prize_name', 'level', 'description', 'quantity']
    search_fields = ['prize_name', 'description']
    list_filter = ['prize_no', 'prize_name', 'description', 'quantity', 'level']
    list_editable = ['publish', 'quantity']
    style_fields = {"description": "ueditor"}


class OrderAdmin(object):
    list_display = ['qq', 'state', 'prize_name', 'number', 'address', 'express', 'operator']
    search_fields = ['prize_name', 'express']
    list_filter = ['state', 'operator', 'date']
    list_editable = ['state', 'operator']


class ForumAdmin(object):
    list_display = ['id', 'user_id', 'type', 'title', 'is_pick', 'tag']
    search_fields = ['user_id', 'title']
    list_filter = ['type', 'is_pick', 'tag']


xadmin.site.register(PointLog, PointLogAdmin)
xadmin.site.register(Prize, PrizeAdmin)
xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(Forum, ForumAdmin)

import xadmin
from PlatForm.models import PointLog, Prize, Order


class PointLogAdmin(object):
    list_display = ['operated_qq', 'state', 'operate_type', 'operate_point', 'description', 'img', 'operator', 'operate_date']
    search_fields = ['description', 'operated_qq__qq']
    list_filter = ['state', 'operate_type', 'operate_point', 'operate_date']
    show_detail_fields = ['img']


class PrizeAdmin(object):
    list_display = ['id', 'prize_no', 'publish', 'prize_name', 'description', 'quantity']
    search_fields = ['prize_name', 'description']
    list_filter = ['prize_no', 'prize_name', 'description', 'quantity']
    list_editable = ['publish', 'quantity']
    style_fields = {"description": "ueditor"}


class OrderAdmin(object):
    list_display = ['qq', 'state', 'prize_name', 'number', 'address', 'express', 'operator']
    search_fields = ['prize_name', 'express']
    list_filter = ['state', 'operator', 'date']
    list_editable = ['state', 'operator']


xadmin.site.register(PointLog, PointLogAdmin)
xadmin.site.register(Prize, PrizeAdmin)
xadmin.site.register(Order, OrderAdmin)

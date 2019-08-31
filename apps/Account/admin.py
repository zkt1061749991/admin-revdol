# 全局配置
import xadmin
from xadmin import views
from .models import Signon, Account

"""
 使用Xadmin的主题功能。
 把全站的配置放在users\admin.py中:
 绑定之后,后台可以选择自己喜欢的主题
"""


class SignonAdmin(object):
    list_display = ['qq', 'password']
    search_fields = ['qq']
    list_filter = []


class AccountAdmin(object):
    list_display = ['qq', 'state', 'name', 'point', 'create_time', 'remark', 'xcxname', 'bilibili']
    search_fields = ['qq2', 'name', 'weixin', 'bilibili', 'remark', 'xcxname']
    list_filter = ['name', 'point', 'state', 'create_time']
    readonly_fields = ['qq', 'point', 'create_time']
    list_editable = ['state']


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '伊莎贝拉后援会贝化值后台管理系统'
    # 修改footer
    site_footer = 'Copyright © 2019 Revdol Systems Incorporated. All rights reserved'
    # 收起菜单
    # menu_style = 'accordion'


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 配置后台主题
    enable_themes = True
    use_bootswatch = True


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(Signon, SignonAdmin)

xadmin.site.register(Account, AccountAdmin)

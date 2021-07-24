# 用户模块的数据

from django.db import models
from django.contrib.auth.models import AbstractUser

"""
# 1.自定义userProfile
"""


class Signon(models.Model):
    qq = models.CharField('QQ号', max_length=255, primary_key=True)
    password = models.CharField('密码', max_length=255)

    class Meta:
        db_table = 'signon'
        verbose_name = '登录账号'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.qq)


class Account(models.Model):
    state_type_choices = (
        (0, '待审核'),
        (1, '正常'),
        (2, '待处理'),
        (3, '兑换中')
    )
    id = models.AutoField(primary_key=True)
    qq = models.ForeignKey(Signon, verbose_name='登录帐号', on_delete=models.CASCADE)
    name = models.CharField('名字', max_length=255, null=True, blank=True)
    point = models.IntegerField(verbose_name='积分')
    state = models.IntegerField(verbose_name='状态', choices=state_type_choices)
    qq2 = models.CharField('QQ', max_length=255, null=True, blank=True)
    weixin = models.CharField('微信', max_length=255, null=True, blank=True)
    bilibili = models.CharField('哔哩哔哩账号', max_length=255, null=True, blank=True)
    xcxuid = models.CharField('小程序uid', max_length=255, null=True, blank=True)
    xcxname = models.CharField('小程序用户名', max_length=255, null=True, blank=True)
    yy = models.CharField('yy号', max_length=255, null=True, blank=True)
    remark = models.TextField('备注信息', max_length=255, null=True, blank=True)
    address = models.TextField('地址信息', max_length=1000, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', null=True, blank=True, auto_now=False)

    class Meta:
        db_table = 'account'
        verbose_name = '用户详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.qq)


class Admin(AbstractUser):
    class Meta:
        db_table = 'admin'
        verbose_name = '后台管理员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.last_name) + str(self.first_name)


class BlackList(models.Model):
    level_type_choices = (
        (0, '需关注'),
        (1, '一般'),
        (2, '严重'),
        (3, '通缉')
    )

    id = models.AutoField(primary_key=True)
    qq = models.CharField('QQ号码或其他社交id', max_length=255)
    name = models.CharField('常用昵称', max_length=255, null=True, blank=True)
    level = models.IntegerField(verbose_name='威胁等级', choices=level_type_choices)
    description = models.TextField(verbose_name='具体描述', max_length=200)
    img = models.ImageField(verbose_name='相关截图', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='记录时间', null=True, blank=True, auto_now=False)
    operator = models.ForeignKey(Admin, verbose_name='记录人', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blacklist'
        verbose_name = '黑名单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Member(models.Model):
    member_sex_type_choices = (
        (1, '男'),
        (2, '女')
    )

    member_official_verify_type_choices = (
        (1, '是'),
        (0, '否')
    )

    id = models.IntegerField(primary_key=True)
    openid = models.CharField('微信openid', max_length=100)
    uid = models.IntegerField('小程序UID')
    sex = models.IntegerField('性别', choices=member_sex_type_choices, null=True, blank=True)
    nickname = models.CharField('昵称', max_length=50, null=True, blank=True)
    birth = models.CharField('生日', max_length=50, null=True, blank=True)
    headimg = models.CharField('头像', null=True, blank=True, max_length=500)
    address = models.TextField('地址信息', null=True, blank=True)
    signature = models.TextField('个性签名', null=True, blank=True)
    status = models.IntegerField('账号状态')
    date = models.DateTimeField('上一次更新时间', auto_now=True)
    official_verify = models.IntegerField('官方认证', choices=member_official_verify_type_choices, null=True, blank=True)

    class Meta:
        db_table = 'member'
        verbose_name = '小程序账号'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Contribute(models.Model):
    contribute_idol_id_type_choices = (
        (1, '卡缇娅'),
        (2, '罗兹'),
        (3, '清歌'),
        (4, '伊莎贝拉'),
        (5, '玉藻'),
        (6, '墨汐')
    )
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField(verbose_name='小程序UID')
    idol_id = models.IntegerField('应援歌姬', choices=contribute_idol_id_type_choices)
    status = models.IntegerField('状态')
    point = models.IntegerField('贡献值')
    user_point = models.IntegerField('贡献值2')
    level = models.IntegerField('等级')
    date = models.DateTimeField('上一次更新时间', auto_now=True)

    class Meta:
        db_table = 'contribute'
        verbose_name = '小程序贡献值'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['uid'])
        ]

    def __str__(self):
        return str(self.id)

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

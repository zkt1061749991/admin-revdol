from django.db import models

from Account.models import Account, Admin, Signon
from DjangoUeditor.models import UEditorField


class PointLog(models.Model):
    operate_type_choices = (
        (0, '扣分'),
        (1, '加分'),
        (2, '过期'),
        (3, '兑换')
    )

    type_type_choices = (
        (0, '二创'),
        (1, '活动'),
        (2, '应援'),
        (3, '福利兑换'),
        (4, '消耗'),
        (5, '其他'),
    )

    operate_state_choices = (
        (0, '登记待评'),
        (1, '有效'),
        (2, '作废'),
        (3, '其他')
    )

    """
    积分日志model
    """
    id = models.AutoField(primary_key=True)
    state = models.IntegerField(verbose_name='状态', choices=operate_state_choices)
    type = models.IntegerField(verbose_name="类别", choices=type_type_choices)
    operated_qq = models.ForeignKey(Signon, verbose_name='操作对象', on_delete=models.CASCADE)
    operate_type = models.IntegerField(verbose_name='操作类型', choices=operate_type_choices)
    operate_point = models.IntegerField(verbose_name='操作点数')
    description = models.TextField(verbose_name='描述', max_length=2000)
    operate_date = models.DateTimeField(verbose_name='操作日期')
    img = models.ImageField(verbose_name='相关截图', null=True, blank=True)
    operator = models.ForeignKey(Admin, verbose_name='操作人', on_delete=models.CASCADE)
    explain = models.TextField(verbose_name='其他说明', max_length=1000, null=True, blank=True)
    remark = models.TextField(verbose_name='管理员备注', max_length=1000, null=True, blank=True)
    forum_id = models.IntegerField(verbose_name='发帖ID', null=True, blank=True)

    class Meta:
        db_table = 'pointlog'
        verbose_name = '贝化值操作'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.operated_qq)


class Prize(models.Model):
    """
    奖品model
    """
    publish_state_type_choices = (
        (0, '隐藏'),
        (1, '公开'),
        (2, '仅作展示')
    )

    prize_level_type_choices = (
        (1, '1N'),
        (2, '2R'),
        (3, '3SR'),
        (4, '4SSR'),
        (5, '5UR')
    )

    id = models.AutoField(primary_key=True)
    prize_no = models.CharField('编号', max_length=255)
    prize_name = models.CharField('名称', max_length=255)
    point = models.IntegerField(verbose_name='兑换价格')
    level = models.IntegerField('稀有度', choices=prize_level_type_choices)
    img = models.ImageField(verbose_name='图片', null=True, blank=True)
    # description = models.TextField(verbose_name='奖品描述', max_length=2000, null=True, blank=True)
    description = UEditorField(verbose_name=u'奖品描述', max_length=2000, width=600, height=200,
                               imagePath="/media/ueditor/", filePath="/media/ueditor/", default='')
    quantity = models.IntegerField(verbose_name='数量')
    publish = models.IntegerField(verbose_name='公开状态', choices=publish_state_type_choices)

    class Meta:
        db_table = 'prize'
        verbose_name = '奖品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.prize_name)


class Order(models.Model):
    """
    兑换记录model
    """
    order_state_type_choices = (
        (0, '申请中'),
        (1, '已发货'),
        (2, '已完成'),
        (3, '已取消')
    )

    id = models.AutoField(primary_key=True)
    qq = models.ForeignKey(Signon, verbose_name='兑换账号', on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, verbose_name='兑换奖品id', on_delete=models.CASCADE, null=True, blank=True)
    prize_name = models.CharField(verbose_name='兑换奖品名称', max_length=255, null=True, blank=True)
    number = models.IntegerField(verbose_name='兑换数量')
    point = models.IntegerField(verbose_name="消耗贝化值")
    address = models.TextField('地址信息', max_length=1000)
    date = models.DateTimeField(verbose_name='兑换日期')
    express = models.CharField('快递信息', max_length=255, null=True, blank=True)
    state = models.IntegerField('订单状态', choices=order_state_type_choices)
    operator = models.ForeignKey(Admin, verbose_name='邮寄负责人', on_delete=models.CASCADE, null=True, blank=True)
    remark = models.TextField(verbose_name='备注信息', max_length=1000, null=True, blank=True)

    class Meta:
        db_table = 'order'
        verbose_name = '兑换订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Forum(models.Model):
    """
    发帖登记model
    """
    forum_type_type_choices = (
        (1, '图文帖'),
        (2, '视频帖')
    )

    forum_is_pick_type_choices = (
        ('NO', '否'),
        ('YES', '已上周赏')
    )

    forum_tag_type_choices = (
        (1, '普通文字帖'),
        (2, '表情包'),
        (3, '同人文'),
        (4, '同人图'),
        (5, 'Cosplay'),
        (6, '手工作品'),
        (7, '普通视频帖'),
        (8, '翻唱翻跳'),
        (9, '二创视频')
    )

    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField('小程序UID')
    type = models.IntegerField('类型', choices=forum_type_type_choices)
    title = models.TextField('标题',max_length=40, null=True, blank=True)
    content = models.TextField('正文', max_length=10000)
    vid = models.CharField('视频链接', max_length=200, null=True, blank=True)
    praise_counts = models.IntegerField('点赞数')
    is_pick = models.CharField('是否上周赏', max_length=10, choices=forum_is_pick_type_choices)
    tag = models.IntegerField('内容标签', choices=forum_tag_type_choices)
    status = models.IntegerField('状态')
    created_time = models.CharField('发帖时间', max_length=100)

    class Meta:
        db_table = 'forum'
        verbose_name = '发帖登记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


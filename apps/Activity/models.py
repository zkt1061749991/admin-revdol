from django.db import models
from Account.models import Admin
from DjangoUeditor.models import UEditorField
# Create your models here.


class Event(models.Model):
    """
        首页图model
        """
    event_state_choices = (
        (0, '准备中'),
        (1, '进行中'),
        (2, '已结束'),
        (3, '已取消')
    )

    event_type_choices = (
        (0, '首页头图'),
        (1, '类型1'),
        (2, '类型2'),
        (3, '类型3'),
        (4, '类型4')
    )

    id = models.AutoField(primary_key=True)
    state = models.IntegerField(verbose_name='状态', choices=event_state_choices)
    type = models.IntegerField(verbose_name='类型', choices=event_type_choices)
    event_title = models.CharField('标题', max_length=100)
    event_alt = models.TextField('简述', max_length=100, null=True, blank=True)
    # event_body = models.TextField(verbose_name='内容', max_length=2000, null=True, blank=True)
    event_body = UEditorField(verbose_name=u'内容', max_length=2000, null=True, blank=True, width=600, height=300,
                              imagePath="/media/ueditor/", filePath="/media/ueditor/", default='')
    img = models.ImageField(verbose_name='首页头图(750×314)', null=True, blank=True)
    url = models.TextField('详情链接', max_length=500, null=True, blank=True)
    begin_date = models.DateTimeField(verbose_name='开始日期')
    end_date = models.DateTimeField(verbose_name='结束日期', null=True, blank=True)
    operator = models.ForeignKey(Admin, verbose_name='操作人', on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'
        verbose_name = '活动宣传'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Receive(models.Model):
    """
    领取记录
    """

    id = models.AutoField(primary_key=True)
    event_code = models.CharField('事件码', max_length=60)
    date = models.DateTimeField(verbose_name='领取日期', auto_now=False)
    qq = models.CharField('领取账号', max_length=255)
    description = models.TextField(verbose_name='描述', max_length=200)

    class Meta:
        db_table = 'receive'
        verbose_name = '奖励领取记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Crowdfunding(models.Model):
    """
    众筹记录
    """

    id = models.AutoField(primary_key=True)
    event_code = models.CharField('事件码', max_length=10)
    date = models.DateTimeField(verbose_name='参与日期', auto_now=False)
    qq = models.CharField('参与账号', max_length=255)
    name = models.CharField('名字', max_length=255, null=True, blank=True)
    point = models.IntegerField(verbose_name='消耗贝化值')
    description = models.TextField(verbose_name='描述', max_length=200)

    class Meta:
        db_table = 'crowdfunding'
        verbose_name = '众筹记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class QQGroup(models.Model):
    """
        领取记录
        """
    qqgroup_state_type_choices = (
        (0, '暂停推送'),
        (1, '正在推送'),
        (2, '特殊')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField('群名称', max_length=100)
    num = models.CharField('群号', max_length=100)
    state = models.IntegerField('推送状态', choices=qqgroup_state_type_choices)
    description = models.TextField(verbose_name='描述', max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'qqgroup'
        verbose_name = 'QQ群信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Topic(models.Model):
    """
        领取记录
        """
    qqgroup_state_type_choices = (
        (0, '暂停'),
        (1, '开放'),
        (2, '结束'),
        (3, '特殊')
    )

    qqgroup_type_type_choices = (
        (0, '活动'),
        (1, '推送'),
        (2, '视频转发'),
        (3, '特殊')
    )

    id = models.AutoField(primary_key=True)
    topic = models.CharField('订阅内容（小程序话题需用##标注）', max_length=100)
    type = models.IntegerField('类型', choices=qqgroup_type_type_choices)
    state = models.IntegerField('状态', choices=qqgroup_state_type_choices)
    point = models.IntegerField('可获取积分')
    description = models.TextField(verbose_name='描述', max_length=200, null=True, blank=True)
    create_time = models.DateTimeField('创建日期', null=True, blank=True)

    class Meta:
        db_table = 'topic'
        verbose_name = '主题订阅'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

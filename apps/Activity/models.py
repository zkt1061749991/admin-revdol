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


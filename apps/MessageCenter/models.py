from django.db import models

from Account.models import Admin
from DjangoUeditor.models import UEditorField


class FeedBack(models.Model):
    """
    反馈信息model
    """

    # 反馈类型
    feedback_type_choices = (
        (0, '官方小妹吐槽与建议'),
        (1, '后援会建议'),
        (2, '说给贝拉的话'),
        (3, '网站运行BUG反馈'),
        (4, '其他')
    )

    feedback_state_choices = (
        (0, '待处理'),
        (1, '已处理'),
        (2, '已失败'),
        (3, '失效')
    )

    id = models.AutoField(primary_key=True)
    qq = models.CharField('QQ号', max_length=255)
    feedback_type = models.IntegerField('反馈类型', choices=feedback_type_choices)
    feedback_body = models.TextField(verbose_name='反馈内容', max_length=2000)
    feedback_date = models.DateTimeField(verbose_name='反馈日期')
    feedback_state = models.IntegerField('处理情况', choices=feedback_state_choices)
    reply = models.TextField(verbose_name='回复内容', max_length=1000, null=True, blank=True)
    deal_date = models.DateTimeField(verbose_name='处理日期', null=True, blank=True, auto_now=True)
    remark = models.TextField(verbose_name='管理员备注', max_length=1000, null=True, blank=True)
    deal_operator = models.ForeignKey(Admin, verbose_name='处理人', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'feedback'
        verbose_name = '反馈信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Notice(models.Model):
    """
    通知信息model
    """
    id = models.AutoField(primary_key=True)
    notice_title = models.CharField('标题', max_length=100)
    notice_alt = models.CharField(verbose_name='预览(20字内加……)', null=True, blank=True, max_length=30)
    # notice_body = models.TextField(verbose_name='内容', max_length=2000)
    notice_body = UEditorField(verbose_name=u'内容', max_length=2000, width=600, height=300, imagePath="/media/ueditor/",
                               filePath="/media/ueditor/", default='')
    notice_date = models.DateTimeField(verbose_name='发布日期')
    operator = models.ForeignKey(Admin, verbose_name='操作人', on_delete=models.CASCADE)

    class Meta:
        db_table = 'notice'
        verbose_name = '系统公告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

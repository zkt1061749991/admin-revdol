# Generated by Django 2.0.7 on 2019-05-25 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MessageCenter', '0003_auto_20190523_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='deal_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='处理日期'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='deal_operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback_state',
            field=models.IntegerField(choices=[(0, '待处理'), (1, '已处理'), (2, '已失败'), (3, '失效')], default=0, verbose_name='处理情况'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='remark',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='管理员备注'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='reply',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='回复内容'),
        ),
    ]

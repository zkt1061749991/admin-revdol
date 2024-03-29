# Generated by Django 2.0.7 on 2019-05-04 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('operate_type', models.IntegerField(choices=[(0, '扣分'), (1, '加分'), (2, '过期'), (3, '兑换')], verbose_name='操作类型')),
                ('operate_point', models.IntegerField(verbose_name='操作点数')),
                ('description', models.TextField(max_length=2000, verbose_name='描述')),
                ('operate_date', models.DateTimeField(auto_now=True, null=True, verbose_name='操作日期')),
                ('operated_qq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.Signon', verbose_name='操作对象')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作人')),
            ],
            options={
                'verbose_name': '积分操作',
                'verbose_name_plural': '积分操作',
                'db_table': 'pointlog',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prize_id', models.CharField(max_length=255, verbose_name='编号')),
                ('prize_name', models.CharField(max_length=255, verbose_name='名称')),
                ('img', models.ImageField(upload_to='', verbose_name='图片')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='奖品描述')),
                ('quantity', models.IntegerField(verbose_name='数量')),
            ],
            options={
                'verbose_name': '奖品信息',
                'verbose_name_plural': '奖品信息',
                'db_table': 'prize',
            },
        ),
    ]

# Generated by Django 2.0.7 on 2019-05-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageCenter', '0002_auto_20190504_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback_type',
            field=models.IntegerField(choices=[(0, '官方小妹吐槽与建议'), (1, '后援会建议'), (2, '说给贝拉的话'), (3, '网站运行BUG反馈'), (4, '其他')], verbose_name='反馈类型'),
        ),
    ]

# Generated by Django 2.0.7 on 2019-05-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20190522_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='state',
            field=models.IntegerField(choices=[(0, '待审核'), (1, '正常'), (2, '待处理'), (3, '兑换中')], verbose_name='状态'),
        ),
    ]

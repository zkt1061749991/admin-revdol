# Generated by Django 2.0.7 on 2019-05-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_account_yy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='创建时间'),
        ),
    ]

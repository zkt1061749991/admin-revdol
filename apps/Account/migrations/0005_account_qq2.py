# Generated by Django 2.0.7 on 2019-07-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20190525_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='qq2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='QQ'),
        ),
    ]

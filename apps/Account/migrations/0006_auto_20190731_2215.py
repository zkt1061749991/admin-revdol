# Generated by Django 2.0.7 on 2019-07-31 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_account_qq2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='qq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.Signon', verbose_name='登录帐号'),
        ),
    ]

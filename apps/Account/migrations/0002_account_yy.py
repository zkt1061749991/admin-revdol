# Generated by Django 2.0.7 on 2019-05-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='yy',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='yy号'),
        ),
    ]
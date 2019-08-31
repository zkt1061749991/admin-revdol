# Generated by Django 2.0.7 on 2019-05-04 19:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='名字')),
                ('point', models.IntegerField(verbose_name='积分')),
                ('state', models.IntegerField(choices=[(0, '待审核'), (1, '正常'), (2, '待处理')], verbose_name='状态')),
                ('weixin', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信')),
                ('bilibili', models.CharField(blank=True, max_length=255, null=True, verbose_name='哔哩哔哩账号')),
                ('xcxuid', models.CharField(blank=True, max_length=255, null=True, verbose_name='小程序uid')),
                ('xcxname', models.CharField(blank=True, max_length=255, null=True, verbose_name='小程序用户名')),
                ('remark', models.TextField(blank=True, max_length=255, null=True, verbose_name='备注信息')),
                ('address', models.TextField(blank=True, max_length=1000, null=True, verbose_name='地址信息')),
                ('create_time', models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户详情',
                'verbose_name_plural': '用户详情',
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Signon',
            fields=[
                ('qq', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='QQ号')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
            ],
            options={
                'verbose_name': '登录账号',
                'verbose_name_plural': '登录账号',
                'db_table': 'signon',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '后台管理员',
                'verbose_name_plural': '后台管理员',
                'db_table': 'admin',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='qq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.Signon', verbose_name='QQ号'),
        ),
    ]
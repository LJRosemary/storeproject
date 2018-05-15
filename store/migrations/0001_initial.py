# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.contrib.auth.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('qq', models.CharField(blank=True, max_length=20, null=True, verbose_name='QQ号码')),
                ('mobile', models.CharField(blank=True, max_length=11, unique=True, null=True, verbose_name='手机号码')),
                ('groups', models.ManyToManyField(to='auth.Group', related_query_name='user', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_query_name='user', blank=True, help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '用户',
                'ordering': ['-id'],
                'verbose_name': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('image_url', models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('index', models.IntegerField(default=1, verbose_name='排列顺序')),
            ],
            options={
                'verbose_name_plural': '广告',
                'ordering': ['index', 'id'],
                'verbose_name': '广告',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='品牌名称')),
                ('index', models.IntegerField(default=1, verbose_name='排列顺序')),
            ],
            options={
                'verbose_name_plural': '品牌',
                'ordering': ['index'],
                'verbose_name': '品牌',
            },
        ),
        migrations.CreateModel(
            name='Caritem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='数量')),
                ('sum_price', models.FloatField(default=0.0, verbose_name='小计')),
            ],
            options={
                'verbose_name_plural': '购物车条目',
                'verbose_name': '购物车条目',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('typ', models.CharField(max_length=20, verbose_name='所属大类')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('index', models.IntegerField(default=1, verbose_name='分类的排序')),
                ('sex', models.IntegerField(default=0, verbose_name='性别')),
            ],
            options={
                'verbose_name_plural': '分类',
                'ordering': ['index', 'id'],
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('old_price', models.FloatField(default=0.0, verbose_name='原价')),
                ('new_price', models.FloatField(default=0.0, verbose_name='现价')),
                ('discount', models.FloatField(default=1, verbose_name='折扣')),
                ('desc', models.CharField(max_length=100, verbose_name='简介')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('num', models.IntegerField(default=0, verbose_name='库存')),
                ('image_url_i', models.ImageField(upload_to='clothing/%Y/%m', default='clothing/default.jpg', verbose_name='展示图片路径')),
                ('image_url_l', models.ImageField(upload_to='clothing/%Y/%m', default='clothing/default.jpg', verbose_name='详情图片路径1')),
                ('image_url_m', models.ImageField(upload_to='clothing/%Y/%m', default='clothing/default.jpg', verbose_name='详情图片路径2')),
                ('image_url_r', models.ImageField(upload_to='clothing/%Y/%m', default='clothing/default.jpg', verbose_name='详情图片路径3')),
                ('image_url_c', models.ImageField(upload_to='clothing/%Y/%m', default='clothing/ce.jpg', verbose_name='购物车展示图片')),
                ('brand', models.ForeignKey(to='store.Brand', verbose_name='品牌')),
                ('category', models.ForeignKey(to='store.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '商品',
                'ordering': ['id'],
                'verbose_name': '商品',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='尺寸')),
                ('index', models.IntegerField(default=1, verbose_name='排列顺序')),
            ],
            options={
                'verbose_name_plural': '尺寸',
                'ordering': ['index'],
                'verbose_name': '尺寸',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='标签')),
            ],
            options={
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
        ),
        migrations.AddField(
            model_name='clothing',
            name='size',
            field=models.ManyToManyField(to='store.Size', verbose_name='尺寸'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='tag',
            field=models.ManyToManyField(to='store.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='caritem',
            name='clothing',
            field=models.ForeignKey(to='store.Clothing', verbose_name='购物车中产品条目'),
        ),
    ]

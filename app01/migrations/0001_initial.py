# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=256)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserType'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='user',
            field=models.ManyToManyField(to='app01.UserInfo'),
        ),
        migrations.AddField(
            model_name='asset',
            name='user_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserGroup'),
        ),
    ]

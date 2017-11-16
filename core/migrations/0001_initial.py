# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('priority', models.CharField(choices=[('HIGH', 'high'), ('NORMAL', 'normal'), ('LOW', 'low')], default='NORMAL', max_length=50)),
                ('progress', models.CharField(choices=[('ASSIGNED', 'assigned'), ('IN_PROGRESS', 'in_progress'), ('TESTED', 'tested'), ('FINISHED', 'finished')], default='ASSIGNED', max_length=50)),
                ('is_finished', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
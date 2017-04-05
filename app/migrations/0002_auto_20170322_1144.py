# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custompermission',
            options={'permissions': (('blog_admin', 'Blog administration'), ('portfolio_admin', 'Portfolio administration'), ('testimonials_admin', 'Testimonials administration'), ('projects_admin', 'Projects administration'), ('user_messages', 'Permission to see customer messages'), ('admin_users', 'Admin users administration'), ('general_users', 'General users administration'), ('comments_admin', 'Comments administration'))},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='nameUA',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='textUA',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contactusmodel',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactusmodel',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='portfoliocontent',
            name='descriptionUA',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='portfoliocontent',
            name='nameUA',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='project',
            name='is_opened',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useryoga',
            name='auth_by_sn',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='useryoga',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useryoga',
            name='extra_data',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

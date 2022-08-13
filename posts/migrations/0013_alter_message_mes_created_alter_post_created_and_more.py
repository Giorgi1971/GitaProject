# Generated by Django 4.0.3 on 2022-03-28 17:30

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0012_post_like_alter_post_created_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='mes_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 21, 30, 28, 234982)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 21, 30, 28, 233981)),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
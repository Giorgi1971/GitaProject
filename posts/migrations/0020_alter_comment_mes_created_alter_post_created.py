# Generated by Django 4.0.3 on 2022-04-01 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_comment_mes_created_alter_post_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='mes_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 0, 25, 58, 423625)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 0, 25, 58, 421625)),
        ),
    ]
